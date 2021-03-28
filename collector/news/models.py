from django.db import models

class News(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    category = models.CharField(max_length=20, default='')
    origin = models.CharField(max_length=20)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.title