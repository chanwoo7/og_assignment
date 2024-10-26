import csv

from django.db.models import Count, Avg, Sum, Q
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from artist.models import ArtistApplication, Artist
from artwork.models import Artwork
from core.views import FilterMixin
from exhibition.models import Exhibition
from user.models import User


class ArtistApplicationListView(FilterMixin, APIView):
    template_name = "management/artist_apply_list.html"
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAdminUser]

    def get(self, request):
        search_field = request.GET.get('search_field', '')  # 드롭다운에서 선택된 검색 필드
        search_query = request.GET.get('q', '')  # 검색어

        # 기본적으로 최신순 정렬
        applications = ArtistApplication.objects.all().order_by('-id')

        # 검색어와 검색 필드가 있는 경우, 해당 필드에서 검색어로 필터링
        applications = self.filter_artists(applications, search_field, search_query)

        return Response({'applications': applications, 'search_field': search_field, 'search_query': search_query},
                        status=status.HTTP_200_OK)


class ProcessApplicationsView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        request_data = request.data
        application_ids = request_data['applications']  # 체크된 신청 ID 리스트
        action = request_data['submitAction']  # 'approve' 또는 'reject'

        if application_ids and action:
            applications = ArtistApplication.objects.filter(id__in=application_ids, status='Pending')

            if action == 'approve':
                # 신청 승인 처리 및 유저의 is_artist 필드 업데이트
                for application in applications:
                    application.status = 'Approved'
                    application.save()

                    # 해당 신청자의 유저 정보 업데이트 (is_artist를 True로 설정)
                    user = application.applicant
                    user.is_artist = True
                    user.save()

                    # Artist 객체 생성하여 해당 유저와 연결
                    artist, created = Artist.objects.get_or_create(
                        user=user,
                        defaults={
                            'name': application.name,
                            'gender': application.gender,
                            'birth_date': application.birth_date,
                            'email': application.email,
                            'contact_number': application.contact_number,
                        }
                    )

            elif action == 'reject':
                applications.update(status='Rejected')

            return JsonResponse({"success": True, "message": "선택한 신청들이 처리되었습니다."}, status=status.HTTP_200_OK)

        return JsonResponse({"success": False, "message": "잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)


class ManagementDashboardView(APIView):
    template_name = "management/dashboard.html"
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 승인 상태에 따른 각각의 신청 수
        pending_applications_count = ArtistApplication.objects.filter(status='Pending').count()
        approved_applications_count = ArtistApplication.objects.filter(status='Approved').count()
        rejected_applications_count = ArtistApplication.objects.filter(status='Rejected').count()

        # 가입된 유저, 작가 수
        total_users_count = User.objects.count()
        total_artists_count = Artist.objects.count()

        # 작품, 전시 수
        total_artworks_count = Artwork.objects.count()
        total_exhibitions_count = Exhibition.objects.count()

        context = {
            'pending_applications_count': pending_applications_count,
            'approved_applications_count': approved_applications_count,
            'rejected_applications_count': rejected_applications_count,
            'total_users_count': total_users_count,
            'total_artists_count': total_artists_count,
            'total_artworks_count': total_artworks_count,
            'total_exhibitions_count': total_exhibitions_count,
        }

        return Response(context, status=status.HTTP_200_OK)


class ArtistStatisticsView(APIView):
    template_name = "management/artist_statistics.html"
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAdminUser]

    def get(self, request):
        today = timezone.now().date()

        # 작가별 통계 계산
        artist_statistics = Artist.objects.annotate(
            # 작품 수
            total_artworks=Count('artwork', distinct=True),
            # 전시 수
            total_exhibitions=Count('exhibition', distinct=True),
            # 진행 중인 전시 수
            ongoing_exhibitions=Count('exhibition',
                                      filter=Q(exhibition__start_date__lte=today, exhibition__end_date__gte=today),
                                      distinct=True),
            # 100호 이하 작품 수
            artworks_below_100_size=Count('artwork', filter=Q(artwork__size__lte=100), distinct=True),
            # 평균 작품 가격
            average_artwork_price=Avg('artwork__price'),
            # 총 작품 가격
            total_artwork_value=Sum('artwork__price', distinct=True)
        )

        return Response({'artist_statistics': artist_statistics}, status.HTTP_200_OK)


class DownloadCSVView(FilterMixin, APIView):
    permission_classes = [IsAdminUser]  # 관리자 권한 설정

    def get(self, request):
        search_field = request.GET.get('search_field', '')  # 드롭다운에서 선택된 검색 필드
        search_query = request.GET.get('q', '')  # 검색어

        # 기본적으로 최신순 정렬
        applications = ArtistApplication.objects.all().order_by('-id')

        # 검색어와 검색 필드가 있는 경우, 해당 필드에서 검색어로 필터링
        applications = self.filter_artists(applications, search_field, search_query)

        # CSV 파일 생성
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="artist_applications.csv"'

        writer = csv.writer(response)
        writer.writerow(['이름', '성별', '생년월일', '이메일', '연락처', '상태', '신청일'])

        for application in applications:
            writer.writerow([
                application.name,
                application.get_gender_display(),
                application.birth_date,
                application.email,
                application.contact_number,
                application.get_status_display(),
                application.submitted_date
            ])

        return response
