from django.db import models
from django.conf import settings


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student_profile'
    )
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    # Add more fields if needed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
