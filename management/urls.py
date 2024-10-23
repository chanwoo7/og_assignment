from django.urls import path
from .views import ArtistApplicationListView, ProcessApplicationsView

urlpatterns = [
    path('applications/', ArtistApplicationListView.as_view(), name='artist_application_list'),
    path('process_applications/', ProcessApplicationsView.as_view(), name='process_applications'),
]