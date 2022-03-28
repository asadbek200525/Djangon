from django.db import models

# Create your models here.

class fanlar(models.Model):
    nomi = models.CharField(max_length=20)
    def __str__(self):
        return self.nomi

class Teacher(models.Model):
    ism = models.CharField(max_length=40)
    fam = models.CharField(max_length=40)
    yosh = models.IntegerField()
    brithday = models.DateTimeField()
    fan = models.ForeignKey(fanlar,on_delete=models.CASCADE,)