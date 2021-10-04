from catalog.models import BoardGames, Category
from django.contrib.auth.models import User
from rest_framework import filters, viewsets
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from myapi.serializers import (BoardGamesSerializer, CategoryGamesSerializer,
                               UserSerializer)


class CategoryGamesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
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
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["rating_from_the_store"]
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
    permission_classes = [AllowAny]

    def get(self, request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth),
        }
        return Response(content)
