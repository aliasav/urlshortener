"""Django admin config for web app
"""
from django.contrib import admin
from web.models import URL

class URLAdmin(admin.ModelAdmin):
    """
    Modeladmin for URL
    """
    list_display = ("id", "short_url", "original_url", "status")
    search_fields = ["short_url", "original_url"]
    readonly_fields = ['created_at',]

admin.site.register(URL, URLAdmin)
