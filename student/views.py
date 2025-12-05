from rest_framework import generics, permissions
from .models import Student
from .serializers import StudentSerializer


class StudentProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return Student.objects.get(user=self.request.user)
