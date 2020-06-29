from django.contrib import admin

from actstream import models

# Use django-generic-admin widgets if available
try:
    from genericadmin.admin import GenericAdminModelAdmin as ModelAdmin
except ImportError:
    ModelAdmin = admin.ModelAdmin


class ActionAdmin(ModelAdmin):
    date_hierarchy = 'timestamp'
    list_display = ('__str__', 'actor', 'verb', 'target', 'public')
    list_editable = ('verb',)
    list_filter = ('timestamp',)
    raw_id_fields = ('actor_content_type', 'target_content_type',
                     'action_object_content_type')


class FollowAdmin(ModelAdmin):
    list_display = ('__str__', 'user', 'follow_object', 'actor_only', 'started')
    list_editable = ('user',)
    list_filter = ('user', 'started',)
    raw_id_fields = ('user', 'content_type')

class ActionEventAdmin(ModelAdmin):
    list_display = ('__str__', 'entity_name', 'message')
    list_editable = ('message',)
    list_filter = ('entity_name', 'message',)
    raw_id_fields = ()

admin.site.register(models.Action, ActionAdmin)
admin.site.register(models.Follow, FollowAdmin)
admin.site.register(models.ActionEvent, ActionEventAdmin)
