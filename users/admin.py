from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')
    search_fields = ('first_name', 'last_name', 'phone')
    ordering = ('last_name', 'first_name')


admin.site.register(User, UserAdmin)
