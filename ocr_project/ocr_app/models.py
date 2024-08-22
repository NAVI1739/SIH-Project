from django.db import models

# Create your models here.
from django.db import models

class HarmfulChemical(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Optional: to provide more info about the chemical

    def __str__(self):
        return self.name
