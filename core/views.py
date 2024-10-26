from datetime import datetime

from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class IndexView(APIView):
    template_name = "index.html"
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return Response(status=status.HTTP_200_OK)


class FilterMixin:
    # 작가 필터링 메서드
    def filter_artists(self, artists, search_field, search_query):
        if search_field and search_query:
            if search_field == 'name':
                artists = artists.filter(name__icontains=search_query)
            elif search_field == 'gender':
                artists = artists.filter(gender=search_query)
            elif search_field == 'birth_date':
                try:
                    # "Y년 m월 d일" 형식을 datetime 객체로 변환
                    search_date = datetime.strptime(search_query, '%Y년 %m월 %d일').date()
                    artists = artists.filter(birth_date=search_date)  # 정확한 날짜 필터링
                except ValueError:
                    # 날짜 형식이 맞지 않을 경우 아무것도 필터링하지 않음
                    artists = artists.none()
            elif search_field == 'email':
                artists = artists.filter(email__icontains=search_query)
            elif search_field == 'contact_number':
                artists = artists.filter(contact_number__icontains=search_query)
        return artists
