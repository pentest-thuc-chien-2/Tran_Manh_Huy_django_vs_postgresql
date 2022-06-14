from django.db import models
from django.utils import timezone
from datetime import datetime,timedelta

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class hospital(models.Model):
    Hospital_id = models.IntegerField(null =False,default=None)
    Hospital_name = models.CharField(max_length=20,null = False)
    Bed_count = models.IntegerField(null = False)
    def __str__(self):
        return f"{self.Hospital_id},{self.Hospital_name},{self.Bed_count}"   
class doctor(models.Model):
    Doctor_id = models.IntegerField(null = False,default=None)
    Doctor_name = models.CharField(max_length=20,null = False)
    Hospital = models.ForeignKey(hospital, null = True, blank = True, on_delete=models.CASCADE)
    Join_date = models.DateTimeField(null = False)
    Speciality = models.CharField(max_length=20,null = False)
    Salary = models.IntegerField(null = False)
    Experience = models.IntegerField(null = True)

    def __str__(self):
        return f"{self.Doctor_id},{self.Doctor_name},{self.Hospital_id},{self.Join_date},{self.Speciality},{self.Salary},{self.Experience}"

