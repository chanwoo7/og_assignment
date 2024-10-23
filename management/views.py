from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from artist.models import ArtistApplication


class ArtistApplicationListView(APIView):
    template_name = "management/artist_apply_list.html"
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAdminUser]  # 관리자 권한 설정

    def get(self, request):
        # 모든 작가 등록 신청 내역을 가져옴, 최신순으로 정렬
        applications = ArtistApplication.objects.all().order_by('-id')
        return Response({'applications': applications}, status=status.HTTP_200_OK)


class ProcessApplicationsView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        application_ids = request.POST.getlist('applications')  # 체크된 신청 ID 리스트
        action = request.POST.get('action')  # 'approve' 또는 'reject'

        print(request.POST)  # 로그 추가

        if application_ids and action:
            applications = ArtistApplication.objects.filter(id__in=application_ids, status='Pending')

            if action == 'approve':
                applications.update(status='Approved')
            elif action == 'reject':
                applications.update(status='Rejected')

            return JsonResponse({"success": True, "message": "선택한 신청들이 처리되었습니다."}, status=status.HTTP_200_OK)

        return JsonResponse({"success": False, "message": "잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)