from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Service, ServiceAdmin)