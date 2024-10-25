from django.urls import path
from .views import ArtistApplicationListView, ProcessApplicationsView, ManagementDashboardView, ArtistStatisticsView

urlpatterns = [
    path('applications/', ArtistApplicationListView.as_view(), name='artist_application_list'),
    path('process_applications/', ProcessApplicationsView.as_view(), name='process_applications'),
    path('dashboard/', ManagementDashboardView.as_view(), name='management_dashboard'),
    path('artist_statics/', ArtistStatisticsView.as_view(), name='artist_statistics'),
]