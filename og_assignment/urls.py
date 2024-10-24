from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('', core_views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('artist/', include('artist.urls')),
    path('management/', include('management.urls')),
    path('artwork/', include('artwork.urls')),
]
