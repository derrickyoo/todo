from django.urls import path

from .views import TaskListView, TaskDetailView


app_name = "tasks"
urlpatterns = [
    path("<int:pk>/", TaskDetailView.as_view(), name="detail"),
    path("", TaskListView.as_view(), name="list"),
]
