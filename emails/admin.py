from emails.models import Email, Confirm
from django.contrib import admin

class EmailAdmin(admin.ModelAdmin):
    list_display = ('from_name', 'from_email', 'to_name', 'to_email', 'subject', 'date', 'sent')
    list_filter = ('date',)
    ordering = ['-date']

class ConfirmAdmin(admin.ModelAdmin):
    list_display = ('uid', 'date', 'confirmed')
    list_filter = ('date',)
    ordering = ['-date']

admin.site.register(Email, EmailAdmin)
admin.site.register(Confirm, ConfirmAdmin)