from django.urls import path
from .views import UserSignUpView, UserSignInView, UserSignOutView

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('signin/', UserSignInView.as_view(), name='signin'),
    path('signout/', UserSignOutView.as_view(), name='signout')
]
