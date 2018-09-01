from rest_framework import serializers
from django.contrib.auth import get_user_model


""" class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validate_data):
        user = get_user_model.objects.create(
            username=validate_data['username']
        )
        user.set_password(validate_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model
        fields = ('username', 'password') """


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = get_user_model
        fields = ('username', 'password', 'email',)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        user.is_superuser = False
        user.save()
        return user

    def update(self, instance, validated_data):
        pass
