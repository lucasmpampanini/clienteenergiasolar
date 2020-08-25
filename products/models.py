from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    image =models.ImageField(upload_to='img_products', blank= True)
    title = models.CharField(max_length=200, unique= True)
    slug = models.SlugField(max_length=200,  unique= True)
    discripition = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title