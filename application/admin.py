from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    # Admin table me show hone wale columns
    list_display = ('id', 'student', 'course', 'status', 'created_at')

    # Filters (sidebar)
    list_filter = ('status', 'created_at')

    # Search bar fields
    search_fields = (
        'student__user__username',   # Student username
        'course__name',              # Course name
    )

    # Default sorting (latest application on top)
    ordering = ('-created_at',)
