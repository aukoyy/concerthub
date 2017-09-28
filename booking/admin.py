from django.contrib import admin
from .models import (
    Artist,
    Concert,
    Festival,
    Stage,
    Bookingoffer,
)

# Register your models here.

admin.site.register(Artist)
admin.site.register(Concert)
admin.site.register(Festival)
admin.site.register(Stage)
admin.site.register(Bookingoffer)
