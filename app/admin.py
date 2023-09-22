from django.contrib import admin
from .models import (
    Client,
    Sponsor,
    Blog,
)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'phone_number')
    list_display_links = ('id', 'fullname', 'phone_number')

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ('id', 'name', 'image')

@admin.register(Blog)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'text', 'date')
    list_display_links = ('id', 'image', 'title', 'text', 'date')
