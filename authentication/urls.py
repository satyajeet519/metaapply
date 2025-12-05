# myapp/urls.py
from django.urls import path
from .views import StudentProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('student/profile/', StudentProfileView.as_view(), name='student_profile'),
]
