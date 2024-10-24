from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions import IsArtist
from exhibition.serializers import ExhibitionSerializer


class ExhibitionRegistrationView(APIView):
    template_name = "exhibition/register.html"
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated, IsArtist]

    def get(self, request):
        artist = request.user.artist
        artworks = artist.artwork_set.all()  # 사용자가 등록한 작품 목록
        return Response({"artworks": artworks}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ExhibitionSerializer(data=request.data)

        if serializer.is_valid():
            artist = request.user.artist
            serializer.save(artist=artist)  # 작가와 연결된 전시로 저장
            return JsonResponse({"success": True}, status=status.HTTP_201_CREATED)

        return JsonResponse({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
