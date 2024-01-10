from rest_framework.generics import CreateAPIView, UpdateAPIView, \
    ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsHuman

from habits.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    """ Контроллер для создания привычки """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    """ Переопределённый метод perform_create() сохраняет \
    текущего пользователя при создании экземпляра привычки """
    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.human = self.request.user
        new_habit.save()


class HabitUpdateAPIView(UpdateAPIView):
    """ Контроллер для редактирования привычки """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsHuman]


class HabitListAPIView(ListAPIView):
    """ Контроллер для просмотра списка привычек текущего пользователя """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator
    """ Переопределённый метод get_queryset() выводит список \
    текущего пользователя """
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(human=self.request.user)


class HabitRetrieveAPIView(RetrieveAPIView):
    """ Контроллер для просмотра одной привычки """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsHuman]


class HabitDeleteAPIView(DestroyAPIView):
    """ Контроллер для удаления привычки """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsHuman]


class HabitIsPublicListAPIView(ListAPIView):
    """ Контроллер для просмотра открытого списка привычек """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator
    """ Переопределённый метод get_queryset() выводит список привычек, \
    которые не скрыты от всех пользователей """
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_public=True)
