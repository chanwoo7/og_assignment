from django.urls import path
from .views import ArtworkRegistrationView

urlpatterns = [
    path('register/', ArtworkRegistrationView.as_view(), name='artwork_register'),
]
