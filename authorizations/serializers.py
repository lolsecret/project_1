from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as BaseTokenObtainPairSerializer,
)



class TokenObtainPairSerializer(BaseTokenObtainPairSerializer):
    username_field = "username"

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        if user.is_active:
            token["username"] = user.username
            token["role"] = user.role


        return token
