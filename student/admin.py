from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'username', 'email', 'phone', 'city', 'created_at')
    search_fields = ('user__username', 'user__email', 'phone', 'city')

    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email

    username.short_description = 'Username'
    email.short_description = 'Email'
