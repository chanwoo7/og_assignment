from django.urls import path
from .views import ArtworkRegistrationView, ArtworkListView

urlpatterns = [
    path('register/', ArtworkRegistrationView.as_view(), name='artwork_register'),
    path('list/', ArtworkListView.as_view(), name='artwork_list')
]
