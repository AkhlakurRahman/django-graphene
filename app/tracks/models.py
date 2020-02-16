from django.db import models
from django.contrib.auth import get_user_model

# Track model


class Track(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    url = models.URLField()
    created_by = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
