from django.urls import path

from .views import TaskListView, TaskDetailView, UserListView, UserDetailView


app_name = "tasks"
urlpatterns = [
    path("users/", UserListView.as_view(), name="user_list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("", TaskListView.as_view(), name="task_list"),
]
