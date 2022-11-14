from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApirestOverview, name="Apirest-overview"),
    path('task-list/', views.TaskList.as_view(), name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-Detail"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-create/', views.taskCreate, name="task-Create"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
    path('task-temporarily-delete/<str:pk>/', views.taskTemporarilyDelete, name="task-temporarily-delete"),
    path('task-restore/<str:pk>/', views.taskRestore, name="task-restore"),
  ]