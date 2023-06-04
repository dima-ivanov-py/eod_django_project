from rest_framework import viewsets

from django.contrib.auth.models import User

from api.v1.endpoints.users.user_serializer import UserSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

