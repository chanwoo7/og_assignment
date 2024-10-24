from django.urls import path
from .views import ArtistApplicationView, ArtistListView

urlpatterns = [
    path('apply/', ArtistApplicationView.as_view(), name='artist_apply'),
    path('list/', ArtistListView.as_view(), name='artist_list'),
]
