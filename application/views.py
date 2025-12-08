from rest_framework import generics, permissions
from .models import Application
from .serializers import ApplicationSerializer
from student.models import Student


class ApplicationListCreateView(generics.ListCreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        student = Student.objects.get(user=self.request.user)
        return Application.objects.filter(student=student)

    def perform_create(self, serializer):
        student = Student.objects.get(user=self.request.user)
        serializer.save(student=student)


class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    permission_classes = [permissions.IsAuthenticated]
