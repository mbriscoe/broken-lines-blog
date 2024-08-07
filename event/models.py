from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    promoter = models.CharField(max_length=200)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.title
