from django.conf import settings
from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    FREQUENCY_CHOICES = (
        ('ONE', 'Раз в день'),
        ('TWO', 'Раз в два дня'),
        ('THREE', 'Раз в три дня'),
        ('FOUR', 'Раз в четыре дня'),
        ('FIVE', 'Раз в пять дней'),
        ('SIX', 'Раз в шесть дней'),
        ('SEVEN', 'Раз в семь дней')
    )
    human = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='habits',
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name='Пользователь'
    )
    location = models.CharField(
        max_length=255, **NULLABLE, verbose_name='Место привычки'
    )
    time = models.TimeField(**NULLABLE, verbose_name='Время привычки')
    action = models.CharField(max_length=255, verbose_name='Действие')
    is_nice = models.BooleanField(
        default=True, verbose_name='Приятная привычка'
    )
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='Связанная привычка'
    )
    frequency = models.CharField(
        max_length=5, default='ONE', choices=FREQUENCY_CHOICES, **NULLABLE
    )
    reward = models.CharField(
        max_length=255, **NULLABLE, verbose_name='Вознаграждение'
    )
    duration = models.PositiveIntegerField(
        **NULLABLE, verbose_name='Время на выполнение'
    )
    is_public = models.BooleanField(default=False, verbose_name='Публичная')

# я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]
    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.location}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
