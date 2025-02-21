from enum import unique

from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.db.models import CharField


class User(AbstractUser):
    pass

class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return self.name

class Course(BaseModel):
    subject = models.CharField(max_length=255)
    description= models.TextField(null=True)
    image = models.ImageField(upload_to=)
    category = models.ForeignKey(Category, on_delete=models.PROTECT())