from django.db import models

# Create your models here.

class Airline(models.Model):
    name = models.CharField(max_length=255)
    websiite = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name


class LuggageRules(models.Model):
    name = models.CharField(max_length=255)
    airline = models.ForeignKey("Airline", on_delete=models.CASCADE)
    display_order = models.PositiveIntegerField()
    is_active = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name


class CancelationRules(models.Model):
    name = models.CharField(max_length=255)
    airline = models.ForeignKey("Airline", on_delete=models.CASCADE)
    display_order = models.PositiveIntegerField()
    is_active = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
