from django.urls import path
from .views import ArtistApplicationView

urlpatterns = [
    path('apply/', ArtistApplicationView.as_view(), name='artist_apply'),
]
