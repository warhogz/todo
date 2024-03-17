from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    CHOICES = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=300, choices=CHOICES)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
