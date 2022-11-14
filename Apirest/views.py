#from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  .serializers import TaskSerializer
from .models import Task
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

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
    
    filter_fields = (
        'date',
        'status',
        'important',
        'is_deleted'
    )

""" 
La fonction ci-dessous va afficher une vue détaillée d'une tâche particulière à l'aide de pk. 
""" 
@api_view(['GET'])
def taskDetail(request, pk):
    tasks = get_object_or_404(Task, pk=pk, is_deleted=False)
    serializer = TaskSerializer(tasks, many = False)
    return Response(serializer.data)

""" 
La fonction ci-dessous va permettre  de modifier une tâche particulière à l'aide de pk. 
""" 
@api_view(['PUT'])
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
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


""" 
La fonction ci-dessous va permettre  de supprimer une tâche particulière à l'aide de pk. 
"""
@api_view(['DELETE'])
def taskTemporarilyDelete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_deleted=True
    task.save()
    return Response("Taks has been deleted temporarily successfully.")

""" 
La fonction ci-dessous va permettre  de supprimer une tâche particulière à l'aide de pk. 
"""
@api_view(['PUT'])
def taskRestore(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_deleted=False
    task.save()
    return Response("Taks has been restore  successfully.")

""" 
La fonction ci-dessous va permettre  de supprimer une tâche particulière à l'aide de pk. 
"""
@api_view(['DELETE'])
def taskDelete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return Response("Taks deleted successfully.")