from django.db import models

class User(models.Model):
    name = models.CharField(max_length=40)
    date = models.DateField()
    adress = models.CharField(max_length=100)
    number = models.IntegerField(default=1)
    def __str__(self):
        return self.name
