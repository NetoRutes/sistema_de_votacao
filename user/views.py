from django.contrib.auth import get_user_model
from django.db import IntegrityError

from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateUserSerializer


class PublicUserViewSet(viewsets.ViewSet):
    permission_classes = ([permissions.AllowAny])

    @list_route(methods=['post'])
    def create_user(self, request):
        """
        Create a new user
        ---
        serializer: CreateUserSerializer
        """
        
        serializer = CreateUserSerializer(data=request.data)
        try:
            if not serializer.is_valid(raise_exception=True):
                return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

            user = serializer.save()
        except IntegrityError:
            data = {"detail": "Username already used."}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        data = {"detail": "User '{}' created!".format(user.username)}
        return Response(data, status=status.HTTP_201_CREATED)
        