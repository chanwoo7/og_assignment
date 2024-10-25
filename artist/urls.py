from django.urls import path
from .views import ArtistApplicationView, ArtistListView, ArtistDashboardView

urlpatterns = [
    path('apply/', ArtistApplicationView.as_view(), name='artist_apply'),
    path('list/', ArtistListView.as_view(), name='artist_list'),
    path('dashboard/', ArtistDashboardView.as_view(), name='artist_dashboard')
]
