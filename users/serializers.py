from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели User """
    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор для регистрации модели User """
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    """ Переопределённый метод create() регистрирует нового пользователя """
    def create(self, validated_data):
        user = User(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
