from django.db import models

# Create your models here.
class EmpRevised(models.Model):
    name = models.CharField(max_length=30)
    rollno = models.IntegerField()
    
    # def __str__(self):
    #     return self.name