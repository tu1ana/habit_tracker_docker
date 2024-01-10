import requests
from django.conf import settings

URL = 'https://api.telegram.org/bot'
TOKEN = settings.TELEGRAM_TOKEN


def send_message(habit):
    url = f'{URL}{TOKEN}/sendMessage'
    data = {
        'chat_id': habit.human.telegram,
        'text': f"It's time you {habit.action} at {habit.time}!"
    }

    requests.post(url, data=data)
