from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Student
from .serializers import StudentSerializer


class StudentProfileView(generics.RetrieveUpdateAPIView):
    """
    GET: fetch logged-in student's profile
    PUT: update logged-in student's profile
    """
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Return student profile for the logged-in user
        student, created = Student.objects.get_or_create(
            user=self.request.user)
        return student
