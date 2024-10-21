from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('', core_views.IndexView.as_view(), name='index'),
    path('user/', include('user.urls')),
]
