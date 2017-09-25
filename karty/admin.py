from django.contrib import admin

from karty.models import ExperimentSettings, User, Task, Card, GIL_data, Session, Task_data, Task_presented, Training
from karty.models import CurrentSettings

class CurrentSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(CurrentSettings, CurrentSettingsAdmin)

admin.site.register(User)
admin.site.register(Task_data)
admin.site.register(Task_presented)
admin.site.register(Training)

class TaskAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Ogólne', {
            'classes': ('collapse',),
            'fields': ('description', 'additional_description', 'task', 'rule',),
        }),
        ('Karta 1', {
            'classes': ('collapse',),
            'fields': ('card1', ),
        }),
        ('Karta 2', {
            'classes': ('collapse',),
            'fields': ('card2', ),
        }),
        ('Karta 3', {
            'classes': ('collapse',),
            'fields': ('card3', ),
        }),
        ('Karta 4', {
            'classes': ('collapse',),
            'fields': ('card4', ),
        }),
    )


admin.site.register(Task, TaskAdmin)
admin.site.register(Card)
admin.site.register(GIL_data)
admin.site.register(Session)

class ExperimentSettingsAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Ogólne', {
            'classes': ('collapse',),
            'fields': ('group_type', ),
        }),
        ('Powitanie', {
            'classes': ('collapse',),
            'fields': ('describtion_phase_1',),
        }),
        ('Etap 1', {
            'classes': ('collapse',),
            'fields': ('describtion_phase_2', 'non_activity_time_GIL_try', 'duration_GIL_try'),
        }),
        ('Etap 2', {
            'classes': ('collapse',),
            'fields': ('describtion_phase_3', 'non_activity_time_GIL', 'duration_GIL'),
        }),
        ('Etap 3', {
            'classes': ('collapse',),
            'fields': ('describtion_phase_4', 'non_activity_time_cards_try', 'duration_cards_try'),
        }),
        ('Etap 4', {
            'classes': ('collapse',),
            'fields': ('describtion_phase_5', 'non_activity_time_cards', 'number_of_sets'),
        })
    )
admin.site.register(ExperimentSettings, ExperimentSettingsAdmin)