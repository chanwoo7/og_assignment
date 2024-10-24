from datetime import datetime

from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from artist.models import ArtistApplication, Artist


class ArtistApplicationListView(APIView):
    template_name = "management/artist_apply_list.html"
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAdminUser]

    def get(self, request):
        search_field = request.GET.get('search_field', '')  # 드롭다운에서 선택된 검색 필드
        search_query = request.GET.get('q', '')  # 검색어

        # 기본적으로 최신순 정렬
        applications = ArtistApplication.objects.all().order_by('-id')

        # 검색어와 검색 필드가 있는 경우, 해당 필드에서 검색어로 필터링
        if search_field and search_query:
            if search_field == 'name':
                applications = applications.filter(name__icontains=search_query)
            elif search_field == 'gender':
                applications = applications.filter(gender=search_query)
            elif search_field == 'birth_date':
                try:
                    # "Y년 m월 d일" 형식을 datetime 객체로 변환
                    search_date = datetime.strptime(search_query, '%Y년 %m월 %d일').date()
                    applications = applications.filter(birth_date=search_date)  # 정확한 날짜 필터링
                except ValueError:
                    # 날짜 형식이 맞지 않을 경우 아무것도 필터링하지 않음
                    applications = applications.none()
            elif search_field == 'email':
                applications = applications.filter(email__icontains=search_query)
            elif search_field == 'contact_number':
                applications = applications.filter(contact_number__icontains=search_query)

        return Response({'applications': applications, 'search_field': search_field, 'search_query': search_query}, status=status.HTTP_200_OK)


class ProcessApplicationsView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        application_ids = request.POST.getlist('applications')  # 체크된 신청 ID 리스트
        action = request.POST.get('action')  # 'approve' 또는 'reject'

        print(request.POST)  # 로그 추가

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
