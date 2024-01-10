from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'location',
        'action',
        'time',
        'related_habit',
        'frequency',
        'reward',
        'duration',
        'is_nice',
        'is_public',
        'human'
    )
