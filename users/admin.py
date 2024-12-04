from django.contrib import admin
from .models import Profile, Contact

# Register your models here.
admin.site.register(Profile)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'created_at')
    search_fields = ('full_name', 'email', 'subject', 'message')
    list_filter = ('created_at',)