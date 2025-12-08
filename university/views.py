from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import CampusSerializer
from .models import Campus
from .models import Course
from django.shortcuts import render
from rest_framework import viewsets
from .models import University
from .serializers import UniversitySerializer
from .serializers import CourseSerializer


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all().order_by('-id')
    serializer_class = UniversitySerializer


class CampusListCreateView(generics.ListCreateAPIView):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
    permission_classes = [IsAuthenticated]  # JWT protected


class CampusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
    permission_classes = [IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
