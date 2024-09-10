from django.db import models

class Jersey(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=2083)
    quantity = models.IntegerField()
    