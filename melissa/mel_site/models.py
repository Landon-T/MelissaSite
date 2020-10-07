from django.db import models





# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=10000)
    category = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.title}"


class Images(models.Model):

    LOGO = 'LOGO'
    IMAGE = 'IMAGE'
    TYPES = (
        (LOGO, 'Logo'),
        (IMAGE, 'Image')
    )

    name= models.CharField(max_length=500)
    image = models.ImageField(upload_to='pictures', default='null')
    category = models.CharField(max_length=5, choices=TYPES, default=IMAGE)

    def __str__(self):
        return self.name


