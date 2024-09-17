from django.db import models
import uuid 

class NewJersey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=2083)
    quantity = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

# class Jersey(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=255)
#     price = models.IntegerField()
#     description = models.TextField()
#     image = models.CharField(max_length=2083)
#     quantity = models.IntegerField()
