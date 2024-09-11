from django.contrib import admin
from .models import Blog, UserMessage, Project


# Customize admin interface for UserMessage model
class UserMessageAdmin(admin.ModelAdmin):
    change_form_template = 'admin/change_form.html'
    list_display = ('first_name', 'last_name', 'email',)

    # Make all fields read-only
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing existing object
            return self.readonly_fields + ('first_name', 'last_name', 'email', 'message',)
        return self.readonly_fields

    # Allow deletion only
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


# Customize admin interface for Project model
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)


# Customize admin interface for Blog model
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)


# Register models with admin site
admin.site.register(Project, ProjectAdmin)
admin.site.register(UserMessage, UserMessageAdmin)
admin.site.register(Blog, BlogAdmin)

# Set admin site headers and titles
admin.site.site_header = 'HZF Admin'
admin.site.site_title = 'Hatua Zetu Foundation'
admin.site.index_title = 'Admin'
