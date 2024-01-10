from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserUpdateAPIView, \
    UserListAPIView, UserRetrieveAPIView, UserDeleteAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('create/', UserCreateAPIView.as_view(), name='create_user'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update_user'),
    path('list/', UserListAPIView.as_view(), name='user_list'),
    path('view/<int:pk>/', UserRetrieveAPIView.as_view(), name='view_user'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='delete_user')
]
