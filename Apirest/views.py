#from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, pagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import json
from rest_framework.viewsets import ModelViewSet
from collections import OrderedDict
from .models import Task
from .serializers import TaskSerializer
from Apirest.pagination import CustomPagination
from rest_framework.permissions import IsAuthenticated

# Create your views here.

"""
Présentation de l'API
"""
@api_view(['GET'])
def ApirestOverview(request):
    Apirest_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/',
    }
    return Response(Apirest_urls)
    
""" 
 la Fonction ci-dessous permet d'afficher toutes les tâches stockées dans la base de données. 
""" 
class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filter_fields = (
        'date',
        'status',
        'important',
        'is_deleted',
        'user'
    )
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        user = self.request.user
        return qs.filter(user=user)

class CustomPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'



""" 
La fonction ci-dessous va afficher une vue détaillée d'une tâche particulière à l'aide de pk. 
""" 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def taskDetail(request, pk):
    tasks = get_object_or_404(Task, pk=pk, is_deleted=False)
    serializer = TaskSerializer(tasks, many = False)
    return Response(serializer.data)

""" 
La fonction ci-dessous va permettre  de modifier une tâche particulière à l'aide de pk. 
""" 
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def taskUpdate(request, pk):
    task = get_object_or_404(Task, pk=pk, is_deleted=False)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

""" 
La fonction ci-dessous va permettre  de créer/ajouter une tâche. 
""" 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


""" 
La fonction ci-dessous va permettre  de supprimer une tâche particulière à l'aide de pk. 
"""
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def taskTemporarilyDelete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    id = task.id
    task.is_deleted=True
    task.save()
    result = {
        "data": id,
        "message": "Taks deleted successfull"
    }
    return Response(result)

""" 
La fonction ci-dessous va permettre  de supprimer une tâche particulière à l'aide de pk. 
"""
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def taskRestore(request, pk):
    task = get_object_or_404(Task, pk=pk)
    id = task.id
    task.is_deleted = False
    task.save()
    result = {
        "data": id,
        "message": "Tasks restore successfull"
    }
    return Response(result)

""" 
La fonction ci-dessous va permettre  de supprimer une tâche particulière à l'aide de pk. 
"""
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def taskDelete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    id = task.id
    task.delete()
    result = {
        "data": id,
        "message": "Taks deleted successfull"
    }
    return Response(result)