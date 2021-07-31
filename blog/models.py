from django.db import models

# Create your models here.
class Blog(models.Model):
    """A class to represent blog"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.title
