from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    student_class = models.CharField(max_length=50)
    rank = models.IntegerField()

    def __str__(self):
        return self.name
