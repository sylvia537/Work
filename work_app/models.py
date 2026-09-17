from django.db import models

# Create your models here.
class About(models.Model):
    header = models.TextField()
    media =models.ImageField(upload_to='img/')
    content = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.header

class Blog(models.Model):
    media =models.ImageField(upload_to='img/')
    header = models.TextField()
    context = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.header