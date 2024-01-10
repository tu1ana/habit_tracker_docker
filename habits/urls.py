from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView,
                          HabitUpdateAPIView,
                          HabitListAPIView,
                          HabitRetrieveAPIView,
                          HabitDeleteAPIView,
                          HabitIsPublicListAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='create_habit'),
    path(
        'update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update_habit'
    ),
    path('', HabitListAPIView.as_view(), name='habit_list'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='view_habit'),
    path(
        'delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='delete_habit'
    ),
    path(
        'public_list/', HabitIsPublicListAPIView.as_view(), name='public_list'
    ),
]
