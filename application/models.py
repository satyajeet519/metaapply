from django.db import models
from django.conf import settings
from student.models import Student
from course.models import Course


class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('submitted', 'Submitted'),
        ('in_review', 'In Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="applications")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="applications")

    remarks = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.course.name}"
