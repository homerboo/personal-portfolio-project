from django.db import models
from datetime import datetime

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='portfolio/images/')  #Folder that its in
    url = models.URLField(blank=True)

