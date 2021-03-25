from django.db import models

class News(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    origin = models.CharField(max_length=20)
    pub_date = models.DateField('date published')
