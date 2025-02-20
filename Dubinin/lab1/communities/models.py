from django.db import models

class Comm(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(max_length=150)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    free = models.BooleanField()
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.name

# Create your models here.
