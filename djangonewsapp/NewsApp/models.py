from django.db import models
from django .utils import timezone
# Create your models here.
class News(models.Model):
    author=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField()
    publish_date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.author
    

class SportsNews(models.Model):
    author=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.author

