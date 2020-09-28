from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=10000)
    category = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.title}"