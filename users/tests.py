from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.test import APITestCase

from users.models import User
from users.views import UserUpdateAPIView


class UserTestCase(APITestCase):
    class HabitTestCase(APITestCase):

        def setUp(self) -> None:
            self.user = User.objects.create(
                email='admin@test.com', password='onetwo', is_staff=True,
                is_superuser=True)
            self.user.save()
            self.client.force_authenticate(user=self.user)

        def test_create_user(self):
            data = {
                'email': 'testuser@test.com',
                'password': 'nineten',
                'phone': '0011223344',
                'city': 'Kathmandu',
                'telegram': settings.TELEGRAM_ID
            }
            # self.test_authentication()
            response = self.client.post(
                '/users/create/', data=data
            )
            print(response.json())

            self.assertEqual(
                response.status_code,
                status.HTTP_201_CREATED
            )

        def test_update_user(self):
            data = {
                'email': 'testuser@test.com'
            }
            UserUpdateAPIView.permission_classes = [AllowAny]
            # self.test_authentication()
            # self.client.force_authenticate()
            response = self.client.patch(
                '/users/update/', data=data
            )
            print(response)

            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )

            self.user.refresh_from_db()

            self.assertEqual(
                self.user.action,
                data['email']
            )

        def test_getting_user_list(self):
            response = self.client.get(
                reverse('users:user_list')
            )

            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )

        def test_retrieve_user(self):
            response = self.client.get(
                reverse('users:view_user', args=[self.user.id])
            )

            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )
