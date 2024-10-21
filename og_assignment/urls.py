from django.urls import path, include

urlpatterns = [
    path('user/', include('user.urls')),  # user 앱의 URL 연결
]
