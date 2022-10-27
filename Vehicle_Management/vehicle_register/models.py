from django.db import models
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
# Create your models here

vehicle_types = [
    ('two_wheeler','two_wheeler'),
    ('three_wheeler','three_wheeler'),
    ('four_wheeler','four_wheeler'),

]

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=20, null=False, validators=[alphanumeric])
    vehicle_type = models.CharField(choices=vehicle_types,max_length=14)
    vehicle_model = models.CharField(max_length=25, null=False)
    vehicle_description = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.vehicle_number