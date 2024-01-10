from celery import shared_task

from habits.models import Habit
from habits.services import send_message


@shared_task
def habit_reminder():
    for habit in Habit.objects.filter(is_nice=False):
        send_message(habit)
