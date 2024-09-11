from django.contrib import admin
from .models import Donation


class DonationAdmin(admin.ModelAdmin):
    change_form_template = 'admin/change_form.html'  # Custom template for change form
    list_display = ('name', 'amount')  # Fields to display in the list view

    def get_readonly_fields(self, request, obj=None):
        if obj:  # When editing an existing object
            return self.readonly_fields + ('name', 'email', 'amount', 'message')
        return self.readonly_fields

    def has_add_permission(self, request):
        return False  # Prevent adding new records

    def has_change_permission(self, request, obj=None):
        return False  # Prevent editing existing records


admin.site.register(Donation, DonationAdmin)
