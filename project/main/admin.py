from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Pictures
# Register your models here.

class AdminConfig(admin.ModelAdmin):
    list_display = ('title', 'author', 'image')

admin.site.register(Pictures, AdminConfig)
admin.site.unregister(Group)