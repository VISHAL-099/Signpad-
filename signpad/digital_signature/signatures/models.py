from django.db import models

class UserSignature(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    signature = models.ImageField(upload_to='signatures/', blank=True, null=True)  # Store signature image

    def __str__(self):
        return self.name
