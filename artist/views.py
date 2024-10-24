from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from artist.serializers import ArtistApplicationSerializer
from core.permissions import IsNotArtist


class ArtistApplicationView(APIView):
    template_name = "artist/apply.html"
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated, IsNotArtist]  # 로그인된 유저 중 작가가 아닌 유저만 접근 가능

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArtistApplicationSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            try:
                serializer.save()
                return JsonResponse({"success": True}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return JsonResponse({"success": False, "errors": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        print(serializer.errors)  # 오류가 있을 때만 이 줄이 실행됨
        return JsonResponse({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
