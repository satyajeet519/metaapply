# from .models import University  # Same app me University hoga
from django.db import models
from django.utils import timezone
# from .models import University  # Remove this line if causing circular import

# FIX: Correct import to avoid circular import
# from university.models import University


class University(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    ranking = models.IntegerField(null=True, blank=True)
    university_type = models.CharField(
        max_length=50,
        choices=[
            ('public', 'Public'),
            ('private', 'Private'),
            ('other', 'Other'),
        ],
        default='public'
    )
    website = models.URLField(null=True, blank=True)
    logo = models.ImageField(
        upload_to='university_logos/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Campus(models.Model):
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        related_name='campuses'
    )
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.university.name}"


class Course(models.Model):
    title = models.CharField(max_length=300)
    university = models.ForeignKey(
        University,
        related_name='courses',
        on_delete=models.CASCADE
    )
    level = models.CharField(
        max_length=50,
        choices=(
            ('UG', 'UG'),
            ('PG', 'PG'),
            ('Diploma', 'Diploma')
        )
    )
    duration = models.CharField(max_length=100, blank=True)
    fees_inr = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )
    description = models.TextField(blank=True)
    intake_months = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.university.name}"
