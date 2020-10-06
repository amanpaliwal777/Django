from django.db import models
from multiselectfield import MultiSelectField


class Enquiry(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()
    course_choise = (
        ('PY', 'Python'),
        ('DJ', 'Django'),
        ('LI', 'Linux'),
        ('OR', 'Oracle')
    )
    course = MultiSelectField(choices=course_choise, max_length=100)
    location_choice = (
        ('ID', 'Indore'),
        ('SWD', 'Sendhwa'),
        ('HYD', 'Hyderabad'),
        ('DH', 'Delhi')
    )
    location = MultiSelectField(choices=location_choice, max_length=100)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    location = models.CharField(max_length=50)
    course = models.CharField(max_length=50)


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    rating = models.IntegerField()
    feedback = models.CharField(max_length=1000)
