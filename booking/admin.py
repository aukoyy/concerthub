from django.contrib import admin

# Register your models here.

from .models import (
    Stage,
    Concert,
)

admin.site.register(Stage)

admin.site.register(Concert)