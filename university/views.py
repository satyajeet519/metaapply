from django.shortcuts import render
from rest_framework import viewsets
from .models import University
from .serializers import UniversitySerializer


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all().order_by('-id')
    serializer_class = UniversitySerializer
