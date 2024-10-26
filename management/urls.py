from django.urls import path
from .views import ArtistApplicationListView, ProcessApplicationsView, ManagementDashboardView, ArtistStatisticsView, DownloadCSVView

urlpatterns = [
    path('applications/', ArtistApplicationListView.as_view(), name='artist_application_list'),
    path('applications/process/', ProcessApplicationsView.as_view(), name='process_applications'),
    path('applications/download/', DownloadCSVView.as_view(), name='download_applications'),
    path('dashboard/', ManagementDashboardView.as_view(), name='management_dashboard'),
    path('artist_statics/', ArtistStatisticsView.as_view(), name='artist_statistics'),
]