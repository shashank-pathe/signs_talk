from django.contrib import admin
from .models import Gesture

# Register the Gesture model with the admin site
@admin.register(Gesture)
class GestureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
