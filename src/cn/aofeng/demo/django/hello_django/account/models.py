from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
    
    userId = models.IntegerField(primary_key=True, unique=True)
    userName = models.CharField(max_length=30, null=False, blank=False, unique=True)
    gender = models.CharField(max_length=1, null=False, blank=False)
    age = models.IntegerField(null=True,default=0)

    def __unicode__(self):
        return "{"+str(self.userId)+","+self.userName+","+self.gender+","+str(self.age)+"}"
