from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    #sign up
    path('register/', RegisterView.as_view()),

    #login using email and password
    #gives access token in response
    path('login/', LoginView.as_view()),
]