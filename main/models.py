from django.db import models

class Jersey(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=2083)
    # models.ImageField(upload_to='jersey_images/')

    # @property
    # def is_mood_strong(self):
    #     return self.mood_intensity > 5