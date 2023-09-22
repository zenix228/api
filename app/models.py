from django.db import models

class Client(models.Model):

    fullname = models.CharField('fullname', max_length=256)
    phone_number = models.CharField('number', max_length=500)

    def __str__(self):
        return f'{self.fullname}'

class Sponsor(models.Model):

    name = models.CharField('name', max_length=256)
    image = models.ImageField('image')

    def __str__(self):
        return f'{self.fullname}'

class Blog(models.Model):
    image = models.ImageField('image')
    title = models.CharField('title', max_length=256)
    text = models.TextField('text')
    date = models.DateTimeField('date', auto_now=True)

    def __str__(self):
        return f'{self.fullname}'
