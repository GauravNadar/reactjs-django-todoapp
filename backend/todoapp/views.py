from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class Home(TemplateView):
    template_name = "build/index.html"


@api_view(['GET'])
def apiOverview(request):
    return Response("API BASE", safe=False)


@api_view(['GET'])
def TaskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def TaskDetail(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def TaskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def TaskUpdate(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def TaskDelete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return Response("Task Deleted Successfully")
