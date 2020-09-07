from django.db import models

# Create your models here.
class Item(models.Model):
    type_is = [("B","Business"), ("C","Couples"), ("S", "Solo travel"), ("F", "Family"), ("G", "Friend's gateway")]
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    type_of_service = models.CharField(max_length=1, choices=type_is, default="B")

    def __str__(self):
        return self.name
