from .models import Course
from django.contrib import admin
from .models import University, Campus


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'university_type', 'ranking')
    search_fields = ('name', 'country', 'city')
    list_filter = ('university_type', 'country')


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'address')
    search_fields = ('name', 'university__name')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'university', 'level', 'fees_inr', 'duration')
    search_fields = ('title', 'university__name')
    list_filter = ('level',)
