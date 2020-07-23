from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import TaskViewSet, UserViewSet


app_name = "tasks"
router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("tasks", TaskViewSet, basename="tasks")

urlpatterns = router.urls
