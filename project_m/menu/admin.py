from django.contrib import admin
from menu.models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'named_url', 'parent')
    list_filter = ('name',)
    search_fields = ('name', 'url', 'named_url')
    ordering = ('name', 'id')

admin.site.register(MenuItem, MenuItemAdmin)