from django.contrib import admin
from .models import (
    Stage,
    Concert,
    Festival,
)

# Register your models here.

admin.site.register(Stage)
admin.site.register(Concert)
admin.site.register(Festival)
