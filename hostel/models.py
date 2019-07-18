from django.db import models

# Create your models here.

class SignUp(models.Model):
    first_name = models.CharField(max_length=50, default='FirstName')
    second_name = models.CharField(max_length=50, null=True, blank=True)
    father_name = models.CharField(max_length=50)