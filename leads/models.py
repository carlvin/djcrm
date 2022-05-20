import imp
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import AbstractUser

# Create your models here.

#User = get_user_model()

class User(AbstractUser):
    pass


class Agent(models.Model):    
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Lead(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    

'''
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES,max_length=100)

    profile_picture = models.ImageField(blank=True,null=True)
    special_files = models.FileField(blank=True,null=True)

    #tuple
  
   SOURCE_CHOICES = (
        ('youtube','youtube'),
        ('google','google'),
        ('newsletter','newsletter'),
    )
    
'''