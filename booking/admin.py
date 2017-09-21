from django.contrib import admin
from .models import (
    Stage,
    Concert,
)

# Register your models here.

admin.site.register(Stage)
admin.site.register(Concert)
