from django.contrib import admin
from .models import Jobs 
class JobsAdmin(admin.ModelAdmin):
    list_display = ('jobs','title', 'slug', 'status','created_on', 'location')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Jobs, JobsAdmin)