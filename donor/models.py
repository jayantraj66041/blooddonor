from django.db import models
from django.contrib.auth.models import User

# Create your models here.

BLOOD_GROUP = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
)

class Donor(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    email = models.EmailField(max_length=100, blank=True, null=True)
    contact = models.IntegerField()
    city = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="Active", choices=(("Active", 'Active'), ("Inactive", "Inactive")))