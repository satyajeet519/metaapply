from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import StudentProfileView

urlpatterns = [
    # JWT Auth
    path('api/auth/login/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Student Profile
    path('api/student/profile/', StudentProfileView.as_view(),
         name='student_profile'),
]
