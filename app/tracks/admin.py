from django.contrib import admin

from .models import Track

# Registering Track model for backend admin.
admin.site.register(Track)
