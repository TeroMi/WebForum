from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.conf import settings
import os
# Create your models here.

class Thread(models.Model):
    CreateDate = models.DateTimeField(blank=False, default=timezone.now)
    EditDate = models.DateTimeField(null=True, blank=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(blank=False, max_length=30, default="Your tile")
    Content = models.ForeignKey('Content', on_delete=models.CASCADE)
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)
    Upvotes = models.IntegerField(default=0)
    Downvotes = models.IntegerField(default=0)

    @classmethod
    def createThread(cls, author, title, content, category):
        thread = cls(Author = author,
        Title = title,
        Content = content,
        Category = category)
        thread.save()
        return thread

class Comment(models.Model):
    SendTime = models.DateTimeField(null=False, blank=False)
    Sender = models.ForeignKey(User, on_delete=models.CASCADE)
    Text = models.TextField()
    Thread = models.ForeignKey('Thread', on_delete=models.CASCADE)
    Upvotes = models.IntegerField(default=0)
    Downvotes = models.IntegerField(default=0)


class CategoryManager(models.Manager):
    def createCategory(self, categoryName):
        category = self.create(Name=categoryName)
        category.save()
        return category

class Category(models.Model):
    Name = models.CharField(max_length=30)
    objects = CategoryManager()
    @classmethod
    def create(cls, name):
        category = cls(Name=name)
        category.save()
        return category

class Content(models.Model):
    Header = models.CharField(max_length=80, blank=False, default="Your header for content")
    Text = models.TextField(blank=False)
    CodeSnippet = models.TextField(blank=True)
    Image = models.ImageField(null=True, blank=True, upload_to='content_images')
    ExternalLink = models.URLField(blank=True)
    @classmethod
    def createContent(cls, header, text, codesnippet, image, link):
        content = cls(
        Header = header,
        Text = text,
        CodeSnippet = codesnippet,
        Image = image,
        ExternalLink = link
        )
        content.save()
        return content
