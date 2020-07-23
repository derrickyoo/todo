from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import TaskListView, UserListView


app_name = "tasks"
router = SimpleRouter()
router.register("users", UserListView, basename="users")
router.register("", UserListView, basename="tasks")

urlpatterns = router.urls
