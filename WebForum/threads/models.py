from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Thread(models.Model):
    CreateDate = models.DateField(null=False, blank=false)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Content = models.CharField(max_length=200)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __init__(self, createDate, author):
        self.CreateDate = createDate
        self.Author = author

class Comment(models.Model):
    SendTime = models.DateField(null=False, blank=false)
    Sender = models.ForeignKey(User, on_delete=models.CASCADE)
    def __init__(self, arg):
        self.
        self.arg = arg

class Category(models.Model):
    Name = models.CharField(max_length=30)

    def createCategory(self, categoryName):
        self.Name = categoryName
