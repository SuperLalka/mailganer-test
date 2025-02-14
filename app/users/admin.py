from django.contrib import admin

from app.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username', 'is_staff', 'is_superuser']
    list_display_links = list_display[:2]
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ['name']
    ordering = ['id']
