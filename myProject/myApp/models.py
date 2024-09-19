# accounts/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50, default='DefaultFirstName')
    lastName = models.CharField(max_length=50, default='DefaultLastName')
    phone_number = models.CharField(max_length=15, default = '0000000000')
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10,default='Other')
    mailId = models.EmailField(default='default@example.com')
    country = models.CharField(max_length=50,default='Unknown')
    address = models.TextField(default='Unknown')
    password = models.CharField(max_length=128)
    class Meta:
        db_table = 'usersregister'
    def __str__(self):
        return self.user.username

class AdminRegister(models.Model):
    admin_code = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    designation = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')])
    email = models.EmailField(max_length=255)
    country = models.CharField(max_length=255)
    address = models.TextField()
    password = models.CharField(max_length=25,default = 'temporary_password')

    class Meta:
        db_table = 'adminregister'

    def __str__(self):
        return self.email

# myApp/models.py

class OrganDonor(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]

    donorname = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    organ = models.CharField(max_length=225)
    age = models.IntegerField()
    contact = models.CharField(max_length=20)
    hospital = models.CharField(max_length=225)
    bloodgroup = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    flag = models.IntegerField(default=False)
    receiver_name = models.CharField(max_length=100, null=True, blank=True)
    receiver_contact = models.CharField(max_length=15, null=True, blank=True)
    receiver_location = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'organ_donors'
