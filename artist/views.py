from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from artist.models import Artist
from artist.serializers import ArtistApplicationSerializer
from core.permissions import IsNotArtist, IsArtist
from core.views import FilterMixin


# 작가 목록 View
class ArtistListView(FilterMixin, APIView):
    template_name = 'artist/list.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        search_field = request.GET.get('search_field', '')
        search_query = request.GET.get('q', '')

        # 최신순 정렬
        artists = Artist.objects.all().order_by('-id')

        # 작가 검색
        artists = self.filter_artists(artists, search_field, search_query)

        return Response({'artists': artists, 'search_field': search_field, 'search_query': search_query},
                        status=status.HTTP_200_OK)


# 작가 등록 신청 View
class ArtistApplicationView(APIView):
    template_name = "artist/apply.html"
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated, IsNotArtist]

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


# 작가 대시보드 View
class ArtistDashboardView(APIView):
    template_name = "artist/dashboard.html"
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated, IsArtist]

    def get(self, request):
        artist = get_object_or_404(Artist, user=request.user)  # 작가 정보 가져오기
        artworks = artist.artwork_set.all().order_by('-id')  # 최신순으로 정렬된 작품 목록
        exhibitions = artist.exhibition_set.all().order_by('-start_date')  # 시작일 기준 정렬된 전시 목록

        context = {
            'artist': artist,
            'artworks': artworks,
            'exhibitions': exhibitions
        }
        return Response(context, status=status.HTTP_200_OK)
