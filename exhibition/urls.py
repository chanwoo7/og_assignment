from django.urls import path
from .views import ExhibitionRegistrationView

urlpatterns = [
    path('register/', ExhibitionRegistrationView.as_view(), name='exhibition_register'),
]
