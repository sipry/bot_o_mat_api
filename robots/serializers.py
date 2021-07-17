from rest_framework import serializers
from robots.models import Type, Task, Robot


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name', 'avatar', 'personality']
        depth = 1


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'description', 'time']
        depth = 1


class RobotReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = ['id', 'name', 'created', 'updated', 'type', 'task']
        depth = 1


class RobotWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = ['id', 'name', 'created', 'updated', 'type', 'task']
