from django.contrib import admin
from .models import UserSignature

@admin.register(UserSignature)
class UserSignatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'signature')  # Display fields in the list view
    search_fields = ('name',)  # Fields to be searchable in the admin interface
    list_filter = ('age',)  # Optional: Add filters for better admin interface usability
    ordering = ('name',)  # Optional: Order by name by default
