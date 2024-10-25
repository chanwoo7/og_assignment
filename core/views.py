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


# 404 에러 처리
def page_not_found(request, exception):
    return render(request, "errors/404.html", {})


# 403 에러 처리
def forbidden(request, exception):
    return render(request, "errors/403.html", {})
