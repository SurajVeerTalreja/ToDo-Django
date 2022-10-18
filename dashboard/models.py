from django import forms
from django.db import models
from django import forms

# Create your models here.
class ToDoList(models.Model):
    entry = models.CharField(max_length=100)
    details = models.TextField()
    is_important = models.BooleanField()

    def __str__(self):
        return self.details
    
    class Meta:
        ordering = ['is_important']