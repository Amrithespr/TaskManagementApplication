from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer, TaskUpdateSerializer
from rest_framework.permissions import IsAuthenticated

class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)

class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

# class TaskReportView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, pk):
#         task = Task.objects.get(pk=pk)
#         user = request.user

#         if user.role in ['admin', 'superadmin'] and task.status == 'completed':
#             return Response({
#                 'completion_report': task.completion_report,
#                 'worked_hours': task.worked_hours
#             })
#         return Response({'error': 'Not authorized or task not completed {task.completion_report}{{user.role}}'}, status=403)

class TaskReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=404)

        user = request.user
        print(f"User: {user.username}, Role: {user.role}, Task Status: {task.status}")

        if user.role in ['admin', 'superadmin'] and task.status == 'completed':
            return Response({
                'completion_report': task.completion_report,
                'worked_hours': task.worked_hours
            }, status=200)

        return Response({
             'error': f'Not authorized or task not completed. Role: {user.role}, Task status: {task.status}'
        }, status=403)
        # return Response({
        #         'completion_report': task.completion_report,
        #         'worked_hours': task.worked_hours
        #     }, status=200)