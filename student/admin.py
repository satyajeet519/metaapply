from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'city', 'email', 'username', 'created_at')
    search_fields = ('user__username', 'phone', 'city')
