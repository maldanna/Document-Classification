from django.db import models
from django.contrib.auth.models import User
#from .models import  Que_csv1
from django.urls import reverse

from PIL import Image


class Profile1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

