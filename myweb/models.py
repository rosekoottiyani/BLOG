from django.db import models

# Create your models here.
class register(models.Model):
    username=models.CharField(default="",max_length=100,unique= True)
    password=models.CharField(default="",max_length=100)
    name=models.CharField(default="",max_length=100)
    email=models.EmailField(default="",max_length=100)
    mobile=models.CharField(default="",max_length=100)
    question=models.CharField(default="",max_length=100)
    answer=models.CharField(default="",max_length=100)

    def __str__(self):
        return self.name

class blog(models.Model):
    username=models.CharField(default="",max_length=100)
    author = models.CharField(default="",max_length=100)
    title = models.CharField(default="",max_length=100)
    blogpost=models.TextField(default="")

