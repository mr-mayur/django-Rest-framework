from django.db import models
from django_countries.fields import CountryField

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'))

class University(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    country = CountryField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    age = models.IntegerField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


