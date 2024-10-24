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
    permission_classes = [IsAuthenticated, IsArtist]

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArtworkSerializer(data=request.data)

        if serializer.is_valid():
            artist = request.user.artist
            serializer.save(artist=artist)  # 작가와 연결된 작품으로 저장
            return JsonResponse({"success": True}, status=status.HTTP_201_CREATED)

        return JsonResponse({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
