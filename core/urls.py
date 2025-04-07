from django.urls import path
from .views import TaskListView, TaskUpdateView, TaskReportView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/report/', TaskReportView.as_view(), name='task-report'),
]
