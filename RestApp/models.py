from django.db import models




class Employee(models.Model):
    empid=models.IntegerField()
    empname=models.CharField()
    email=models.CharField()


    def __str__(self):
        return self.empname





