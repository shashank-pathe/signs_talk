from django.db import models

class Gesture(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='gestures/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name