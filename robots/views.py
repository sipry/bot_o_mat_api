import random
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from robots.models import Type, Task, Robot
from robots.serializers import RobotWriteSerializer,  RobotReadSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def robot(request, robot_pk=None):
    if request.method == 'GET':
        if robot_pk:
            resp = Robot.objects.get(id=robot_pk)
            serializer = RobotReadSerializer(resp, many=False)
            return Response(serializer.data)
        else:
            resp = Robot.objects.all()
            serializer = RobotReadSerializer(resp, many=True)
            return Response(serializer.data)
    elif request.method == 'PUT':
        try:
            robot = Robot.objects.get(id=robot_pk)
        except Robot.DoesNotExist:
            return HttpResponse(status=404)

        data = JSONParser().parse(request)
        serializer = RobotWriteSerializer(robot, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'POST':
        if 'type' not in request.data:
            # generate a random type
            type_list = list(Type.objects.all().values())
            random_type = random.sample(type_list, 1)
            random_type_id = list(map(lambda x: x.get("id"), random_type))
            request.data['type'] = random_type_id[0]
        # generate a array of 5 random tasks
        task_list = list(Task.objects.all().values())
        random_task = random.sample(task_list, 5)
        random_task_id = list(map(lambda x: x.get("id"), random_task))
        request.data['task'] = random_task_id
        serializer = RobotWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        resp = Robot.objects.get(id=robot_pk)
        resp.delete()
        return HttpResponse(status=204)