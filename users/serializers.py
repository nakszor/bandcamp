from rest_framework import serializers
from .models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="A user with that username already exists.")],
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="This field must be unique.")],
    )
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data, is_superuser=True)
        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
            if key == 'password':
                instance.set_password(value)
        instance.save()
        return instance
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_superuser': {'read_only': True}
        }


