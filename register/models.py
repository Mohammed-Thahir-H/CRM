from django.db import models

# Create your models here.

class Register(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    #DateOfBirth = models.DateField()
    Email = models.EmailField()
    PhoneNo = models.IntegerField()
    Password = models.CharField(max_length=20)

    def __str__(self):
     return self.Firstname +' '+ self.Lastname