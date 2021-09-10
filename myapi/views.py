from catalog.models import BoardGames, Category
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from myapi.serializers import (BoardGamesSerializer, CategoryGamesSerializer,
                               UserSerializer)


class CategoryGamesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategoryGamesSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth),
        }
        return Response(content)


class BoardGamesViewSet(viewsets.ModelViewSet):
    queryset = BoardGames.objects.all().order_by("name")
    serializer_class = BoardGamesSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth),
        }
        return Response(content)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth),
        }
        return Response(content)
