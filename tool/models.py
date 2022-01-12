from django.db import models
from django.urls import reverse


# Create your models here.


class Task(models.Model):
	
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["created"]

    def __str__(self):
	    return self.title
    