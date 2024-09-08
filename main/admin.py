from django.contrib import admin
from .models import Jersey

class JerseyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'quantity')

admin.site.register(Jersey, JerseyAdmin)
