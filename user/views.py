from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSignupSerializer


class UserSignUpView(APIView):
    template_name = "user/signup.html"
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"success": True}, status=status.HTTP_201_CREATED)

        return JsonResponse({"success": False, "errors": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class UserSignInView(APIView):
    template_name = "user/signin.html"
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"success": True}, status=200)
        else:
            return JsonResponse({"success": False, "error": "잘못된 아이디 또는 비밀번호입니다."},
                                status=status.HTTP_400_BAD_REQUEST)


class UserSignOutView(APIView):
    def post(self, request):
        logout(request)
        return JsonResponse({"success": True}, status=status.HTTP_200_OK)
