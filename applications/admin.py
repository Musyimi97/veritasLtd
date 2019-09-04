from django.contrib import admin

from .models import Applications
# Register your models here.
class ApplicationsAdmin(admin.ModelAdmin):
    list_display=('name', 'history', 'resume', 'phone')
    list_filter=('resume',)
    search_fields=['email', 'phone', 'name', ]


admin.site.register(Applications,ApplicationsAdmin)