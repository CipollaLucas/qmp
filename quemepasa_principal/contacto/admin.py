from django.contrib import admin
from .models import ContactoModelo
# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('nombre', 'email', 'created')
    ordering = ('created',)
    date_hierarchy = 'created'
    list_filter = ('created',)

admin.site.register(ContactoModelo, ContactoAdmin)