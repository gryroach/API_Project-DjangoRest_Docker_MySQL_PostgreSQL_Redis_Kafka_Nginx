from django.contrib import admin
from .models import LogRecord


@admin.register(LogRecord)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'type_of_sync')
