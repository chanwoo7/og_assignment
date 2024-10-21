from django.urls import path
from .views import UserSignupView, UserSigninView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('signin/', UserSigninView.as_view(), name='signin')
]
