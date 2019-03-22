from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Guild(models.Model):
    name = models.CharField(max_length=45)
    tag = models.CharField(max_length=10)
    tapi_key = models.CharField(max_length=45, blank=True)
    tchat_id = models.CharField(max_length=45, blank=True)
    dapi_key = models.CharField(max_length=45, blank=True)
    dchat_id = models.CharField(max_length=45, blank=True)

    def __str__(self):
        return f'{self.name} [{self.tag}]'

class Profile(models.Model):
    name = models.CharField(max_length=45)
    guild = models.ForeignKey(Guild,
                            on_delete=models.CASCADE,
                            related_name='profiles')
    def __str__(self):
        return self.name

class Entity(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=240)
    permission = models.CharField(max_length=1)
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='entities')

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    profile = models.ForeignKey(Profile,
                                on_delete=None)
                                
    guild = models.ForeignKey(Guild,
                            on_delete=models.CASCADE,
                            related_name='members')
