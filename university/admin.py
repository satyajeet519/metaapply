from django.contrib import admin
from .models import University


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'university_type')
    search_fields = ('name', 'country', 'city')
    list_filter = ('country', 'university_type')
