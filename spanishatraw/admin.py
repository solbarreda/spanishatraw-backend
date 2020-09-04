"""Admin reusable."""

from django.contrib import admin


class ReadOnlyAdminMixin(admin.ModelAdmin):
    """Disables all editing capabilities."""

    change_form_template = "admin/view.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_actions(self, request):
        """Get model admin actions."""
        actions = super().get_actions(request)
        del_action = "delete_selected"
        if del_action in actions:
            del actions[del_action]
        return actions

    def has_add_permission(self, request):
        """Has add permission."""
        return False

    def has_delete_permission(self, request, obj=None):
        """Has delete permission."""
        return False

    def save_model(self, request, obj, form, change):
        """Save model."""
        pass

    def delete_model(self, request, obj):
        """Delete model."""
        pass

    def save_related(self, request, form, formsets, change):
        """Save related models."""
        pass
