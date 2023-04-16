from django.db import models
from django.contrib.auth.models import User
import uuid


# for choices of gender
GENDER_CHOICES = (
        ('M', 'Male', ), 
        ('F', 'Female', ), 
        ('Other',"Other"),
    )



# Create your models here.
class Patient(models.Model):
    # storing detials of patient (user)
    
    patUserName=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=50,default='unknown')
    mobile=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=16)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=10)
    AccountCreatedOn=models.DateTimeField(auto_now_add=False)# automatically add date on which the object is created
    
    class Meta:
        # meta data
        # telling django to sort the data on column 
        ordering=['-AccountCreatedOn']

    def __str__(self):
        return self.name

class Doctor(models.Model):
    # storing details of doctors (user)
    
    docUserName=models.CharField(max_length=50,primary_key=True)#primary key
    name=models.CharField(max_length=50,default='unknown')
    mobile=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=16)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=10)
    description=models.CharField(max_length=200)
    degree=models.CharField(max_length=200,default="none")
    specialization=models.CharField(max_length=200,default="none")
    experience=models.IntegerField()
    AccountCreatedOn=models.DateTimeField(auto_now_add=False)# automatically add date on which the object is created
    updatedOn=models.DateTimeField(auto_now=False)# automatically add date on which it is last updated


    class Meta:
        # meta data
        # telling django to sort the data on column 
        ordering=['-AccountCreatedOn']

    def __str__(self):
        return self.name

class Appointment(models.Model):
    # storing details of doctors (user)
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)# primary key
    docUserName=models.ForeignKey(Doctor,on_delete=models.CASCADE)# foreign key
    patUserName=models.ForeignKey(Patient,on_delete=models.CASCADE)# foreign key
    disease=models.CharField(max_length=500)
    bloodGroup=models.CharField(max_length=5,null=True,blank=True)
    appointmentDate=models.DateField(max_length=10)# appointment on
    appointmentTime=models.TimeField(max_length=10)# appointment time
    formFilled=models.DateTimeField(auto_now_add=True)# form filled on
    status=models.BooleanField()

    def __str__(self):
        return self.patUserName+" have appoinment with "+self.docUserName
