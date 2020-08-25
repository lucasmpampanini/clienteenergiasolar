from django.db import models

class Service(models.Model):
    image =models.ImageField(upload_to='img_services', blank= True)
    title = models.CharField(max_length=200, unique= True)
    slug = models.SlugField(max_length=200,  unique= True)
    discripition = models.TextField()

    def __str__(self):
        return self.title
