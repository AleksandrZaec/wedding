from django.contrib import admin
from .models import Media
from .services import delete_from_storage


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        if obj.file:
            file_name = obj.file.name
            delete_from_storage(file_name)
            obj.file.delete(save=False)
        super().delete_model(request, obj)

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            if obj.file:
                file_name = obj.file.name
                delete_from_storage(file_name)
                obj.file.delete(save=False)
        super().delete_queryset(request, queryset)
