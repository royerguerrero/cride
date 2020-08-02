"""Cicles admin"""

# Django
from django.contrib import admin

# Models
from cride.circles.models import Circle

@admin.register(Circle)
class CirclesAdmin(admin.ModelAdmin):
    """Circles model admin"""

    list_display = (
        'slug_name',
        'name',
        'is_public',
        'verified',
        'is_limited',
        'members_limit',
    )

    search_fields = ('slug_name', 'name')
    list_filter = (
        'is_public',
        'verified',
        'is_limited',
    )