from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length = 20)
    phone = models.IntegerField()
    designation = models.CharField(max_length = 15)

    def __str__(self):
        return self.emp_name
