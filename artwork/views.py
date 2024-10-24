from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from artwork.models import Artwork
from artwork.serializers import ArtworkSerializer
from core.permissions import IsArtist


class ArtworkListView(APIView):
    template_name = 'artwork/list.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        search_field = request.GET.get('search_field', '')
        search_query = request.GET.get('q', '')  # 제목 검색용
        min_value = request.GET.get('min_value', '')  # 범위 검색용 최소값
        max_value = request.GET.get('max_value', '')  # 범위 검색용 최대값

        # 기본적으로 최신순 정렬
        artworks = Artwork.objects.all().order_by('-id')

        # 검색 기능
        if search_field == 'title' and search_query:
            artworks = artworks.filter(title__icontains=search_query)
        elif search_field == 'artist_name' and search_query:
            # 작가명 검색 기능 추가
            artworks = artworks.filter(artist__name__icontains=search_query)
        elif search_field == 'price':
            if min_value and max_value:
                try:
                    min_value = float(min_value)
                    max_value = float(max_value)
                    artworks = artworks.filter(price__gte=min_value, price__lte=max_value)
                except ValueError:
                    artworks = artworks.none()
        elif search_field == 'size':
            if min_value and max_value:
                try:
                    min_value = int(min_value)
                    max_value = int(max_value)
                    artworks = artworks.filter(size__gte=min_value, size__lte=max_value)
                except ValueError:
                    artworks = artworks.none()

        return Response({'artworks': artworks, 'search_field': search_field, 'search_query': search_query,
                         'min_value': min_value, 'max_value': max_value}, status=status.HTTP_200_OK)


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
