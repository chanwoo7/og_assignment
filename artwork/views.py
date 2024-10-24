from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from artwork.serializers import ArtworkSerializer
from core.permissions import IsArtist


class ArtworkRegistrationView(APIView):
    template_name = "artwork/register.html"
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated, IsArtist]  # 로그인된 사용자만 접근 가능

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        # POST 요청 시 데이터 유효성 검사 및 저장
        serializer = ArtworkSerializer(data=request.data)

        if serializer.is_valid():
            try:
                # User와 연결된 Artist가 존재하는지 확인
                artist = request.user.artist
                serializer.save(artist=artist)  # 작가와 연결된 작품으로 저장
                return JsonResponse({"success": True}, status=status.HTTP_201_CREATED)
            except ObjectDoesNotExist:
                return JsonResponse({"success": False, "errors": "작가 정보가 존재하지 않습니다."},
                                    status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
