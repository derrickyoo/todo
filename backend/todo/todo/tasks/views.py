from django.contrib.auth import get_user_model

from rest_framework import viewsets

from .models import Task
from .permissions import IsAuthorOrReadOnly
from .serializers import TaskSerializer, UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
