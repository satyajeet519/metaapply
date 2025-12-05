from django.db import models


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
