from django.urls import path, include
from api.views.auth.signup_view import RegisterUserView
from api.views.auth.verify_otp_view import VerifyOtp

urlpatterns = [
  path('auth/signup/', RegisterUserView.as_view(), name='signup'), 
  path('auth/verify', VerifyOtp.as_view(), name='verify_otp'),
]