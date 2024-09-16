from django.contrib import admin
from .models import NewJersey

class JerseyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'quantity')

admin.site.register(NewJersey, JerseyAdmin)
