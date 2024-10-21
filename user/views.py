from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSignupSerializer


class UserSignupView(APIView):
    template_name = "user/signup.html"
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"success": True}, status=status.HTTP_201_CREATED)

        return JsonResponse({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# class UserSigninView(APIView):
#     template_name = "user/signin.html"
#     renderer_classes = [TemplateHTMLRenderer]
#
#     def get(self):