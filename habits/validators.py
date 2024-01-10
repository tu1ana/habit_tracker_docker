from rest_framework import serializers


frequency = ('ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN')


def validate_related_habit_and_reward(value):
    if value.get('related_habit') and value.get('reward'):
        raise serializers.ValidationError(
            'Одновременный выбор связанной привычки и \
            указания вознаграждения невозможен!'
        )


def validate_duration(value):
    if value.get('duration') > 120:
        raise serializers.ValidationError(
            'Время выполнения должно быть не больше 120 секунд!'
        )


def validate_related_habit(value):
    if 'related_habit' in value and not value.get('related_habit').is_nice:
        raise serializers.ValidationError(
            'В связанные привычки могут попадать \
            только привычки с признаком приятной привычки!'
        )


def validate_nice_habit(value):
    if value.get('reward') or value.get('related_habit'):
        raise serializers.ValidationError(
            'У приятной привычки не может быть \
            вознаграждения или связанной привычки!'
        )


def validate_frequency(value):
    if value.get('frequency') not in frequency:
        raise serializers.ValidationError(
            'Нельзя выполнять привычку реже, чем 1 раз в 7 дней!'
        )
