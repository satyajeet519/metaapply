from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics, permissions
from student.models import Student
from student.serializers import StudentSerializer

# Student Profile API


class StudentProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StudentSerializer

    def get_object(self):
        # Logged-in user ka student profile return kare
        return self.request.user.student_profile
