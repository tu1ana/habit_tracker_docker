from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, UpdateAPIView, \
    ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from users.models import User
from users.permissions import IsAuthUser
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """ Контроллер для создания пользователя """
    serializer_class = UserSerializer

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]


class UserUpdateAPIView(UpdateAPIView):
    """ Контроллер для редактирования пользователя """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, IsAuthUser]


class UserListAPIView(ListAPIView):
    """ Контроллер для просмотра списка пользователей """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(RetrieveAPIView):
    """ Контроллер для просмотра одного пользователя """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDeleteAPIView(DestroyAPIView):
    """ Контроллер для удаления пользователя """
    queryset = User.objects.all()
    permission_classes = [IsAdminUser, IsAuthUser]
