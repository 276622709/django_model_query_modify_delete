from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Student(models.Model):
        name=models.CharField(max_length=20)
        age=models.IntegerField(max_length=3)


class Subject(models.Model):
        student=models.ForeignKey(Student)
        sub_name=models.CharField(max_length=20)
        sub_num=models.IntegerField(default=0)
