from django.urls import path

from .views import Home, TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('', Home.as_view()),
    path('task-list/', TaskList, name='task-list'),
    path('task-detail/<int:id>/', TaskDetail, name='task-detail'),
    path('task-create/', TaskCreate, name='task-create'),
    path('task-update/<int:id>/', TaskUpdate, name='task-update'),
    path('task-delete/<int:id>/', TaskDelete, name='task-delete'),

]
