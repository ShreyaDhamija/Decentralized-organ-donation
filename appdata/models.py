from django.db import models

# Create your models here.
class Doctor(models.Model):
    dname=models.CharField( max_length=50)
    quali=models.CharField( max_length=50)
    spec=models.CharField( max_length=50)
    hname=models.CharField( max_length=50)
    place=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    cno=models.CharField( max_length=50)
    uname=models.CharField( max_length=50)
    pass1=models.CharField( max_length=50)
class Donor(models.Model):
    dname=models.CharField( max_length=50)
    rname=models.CharField( max_length=50)
    addr=models.CharField( max_length=50)
    dob=models.CharField( max_length=50)
    gender=models.CharField( max_length=50)
    bgroup=models.CharField( max_length=50)
    organ=models.CharField( max_length=50)
    occ=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    cno=models.CharField( max_length=50)
    ddate=models.CharField( max_length=50)
    st=models.CharField( max_length=50)
    hash=models.CharField( max_length=500)
class Patient(models.Model):
    pname=models.CharField( max_length=50)    
    gender=models.CharField( max_length=50)
    dob=models.CharField( max_length=50)
    place=models.CharField( max_length=50)
    street=models.CharField( max_length=50)
    pcode=models.CharField( max_length=50)
    cno=models.CharField( max_length=50)    
    bgroup=models.CharField( max_length=50)
    organ=models.CharField( max_length=50)
    dname=models.CharField( max_length=50)
    demail=models.CharField( max_length=50)
    hname=models.CharField( max_length=50)
    st=models.CharField( max_length=50)
    hash=models.CharField( max_length=500)
    
    
    
    
   