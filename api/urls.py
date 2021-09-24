from django.urls import path, include
from api.views.auth.signup_view import RegisterUserView
from api.views.auth.verify_otp_view import VerifyOtp
from api.views.auth.login_view import LoginView
from api.views.term.term_view import TermView
from api.views.classe.classe_view import ClasseView
from api.views.subject.subject_view import SubjectView

urlpatterns = [
  path('auth/signup/', RegisterUserView.as_view(), name='signup'), 
  path('auth/verify/', VerifyOtp.as_view(), name='verify_otp'),
  path('auth/login/', LoginView.as_view(), name='login'),
  path('term/', TermView.as_view(), name='term'),
  path('classe/<uuid:pk>/', ClasseView.as_view(), name='classe'),
  path('subject/<uuid:pk>/', SubjectView.as_view(), name='subject'),
]