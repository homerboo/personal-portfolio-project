from django.db import models
from datetime import date, datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    dateCreated = models.DateField(default=datetime.now)
    content = models.TextField()