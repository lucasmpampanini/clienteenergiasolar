from django.db import models

class Faq(models.Model):
    pergunta = models.CharField(max_length=200, unique=True)
    resposta = models.TextField()

    def __str__(self):
        return self.pergunta


class HomeImg(models.Model):
    image =models.ImageField(upload_to='img_home', blank= True)
    title = models.CharField(max_length=200, unique= True)

    def __str__(self):
        return self.title