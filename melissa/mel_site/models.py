from django.db import models





# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=10000)
    category = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.title}"


class Images(models.Model):



    name= models.CharField(max_length=500)
    image = models.ImageField(upload_to='pictures', default='null')
    

    def __str__(self):
        return self.name


class Sponsor(models.Model):

    TIER1 = 'TIER1'
    TIER2 = 'TIER2'
    TIER3 = 'TIER3'
    
    TIER_LIST = (
        (TIER1, 'Tier 1'),
        (TIER2, 'Tier 2'),
        (TIER3, 'Tier 3')
    )

    name= models.CharField(max_length=1000)
    image = models.ImageField(upload_to='pictures', default='null')
    url = models.CharField(max_length=1000 )
    tier = models.CharField(max_length=5, choices=TIER_LIST, default=TIER3)

    def __str__(self):
        return self.name