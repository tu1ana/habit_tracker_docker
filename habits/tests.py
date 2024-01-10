from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.habit = Habit.objects.create(
            location='test',
            time='18:00',
            action='test',
            is_nice='False',
            frequency='ONE',
            reward='test',
            duration='100',
            is_public='True',
        )
        self.user = User.objects.create(
            email='test@example.com'
        )
        self.client = APIClient()
        # self.client.force_authenticate(user=self.user)
        self.user = User.objects.create(
            email='admin@test.com', password='onetwo', is_staff=True,
            is_superuser=True, telegram=settings.TELEGRAM_ID)
        self.client.force_authenticate(user=self.user)

    def test_authentication(self):
        user = User.objects.create(
            email='test@site.com', password='onetwo', is_staff=True,
            is_superuser=True
        )
        # self.client.force_authenticate(user=user)
        user.save()

    def test_create_habit(self):
        data = {
            'location': 'garden',
            'time': '18:00',
            'action': 'dance',
            'is_nice': True,
            'frequency': 'ONE',
            'duration': 100,
            'is_public': True
        }
        # self.test_authentication()
        response = self.client.post(
            reverse('habits:create_habit'),
            data
        )
        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            2,
            Habit.objects.all().count()
        )

    def test_update_habit(self):
        data = {
            'action': 'new_dance'
        }
        # self.test_authentication()
        self.client.force_authenticate()
        response = self.client.patch(
            reverse('habits:update_habit', args=[self.habit.pk]),
            data
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.habit.refresh_from_db()

        self.assertEqual(
            self.habit.action,
            data['action']
        )

    def test_getting_habit_list(self):
        response = self.client.get(
            reverse('habits:habit_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 0,
                "next": None,
                "previous": None,
                "results": []
            }
        )

    def test_retrieve_habit(self):
        response = self.client.get(
            reverse('habits:view_habit', args=[self.habit.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['action'], 'jump'
        )

    def test_delete_habit(self):
        data = {
            'id': self.habit.id,
            'location': 'garden',
            'time': '18:00',
            'action': 'dance',
            'is_nice': True,
            'frequency': 'ONE',
            'duration': 100,
            'is_public': True
        }
        response = self.client.post(
            reverse('habits:create_habit', data)
        )

        response = self.client.delete(
            reverse('habits:delete_habit', args=[self.habit.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
