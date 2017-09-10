from django.contrib import admin

# Register your models here.

from .models import Manufacturer, LaunchPlatform, Engine

admin.site.register(Manufacturer)
admin.site.register(LaunchPlatform)
admin.site.register(Engine)
