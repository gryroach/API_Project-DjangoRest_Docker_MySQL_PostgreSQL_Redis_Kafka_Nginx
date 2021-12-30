from django.contrib import admin
from .models import JPHModel


@admin.register(JPHModel)
class JPHAdmin(admin.ModelAdmin):
    list_display = ('id', 'update_date')
