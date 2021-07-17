from django.db import models


class Task(models.Model):
    description = models.TextField()
    time = models.IntegerField()

    def __str__(self):
        return self.description


class Type(models.Model):
    name = models.CharField(max_length=250)
    avatar = models.CharField(max_length=250, null=True)
    personality = models.CharField(max_length=250)


class Robot(models.Model):
    name = models.CharField(max_length=250)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    task = models.ManyToManyField(Task)


