from rest_framework import serializers

from habits.models import Habit
from habits.validators import (validate_related_habit_and_reward,
                               validate_duration,
                               validate_related_habit,
                               validate_nice_habit,
                               validate_frequency)


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор модели Habit """
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            validate_related_habit_and_reward,
            validate_duration,
            validate_related_habit,
            validate_nice_habit,
            validate_frequency
        ]
