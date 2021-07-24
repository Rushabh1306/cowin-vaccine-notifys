
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class StatesList(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)

    class Meta:
        db_table = "statelist"

    def __str__(self) -> str:
        return self.state_name

class DistrictList(models.Model):
    district_id = models.IntegerField(primary_key=True)
    district_name = models.CharField(max_length=100)
    state_id = models.IntegerField()

    class Meta:
        db_table = "districtlist"

    def __str__(self) -> str:
        return self.district_name



class UserFilter(models.Model):
    email = models.EmailField()
    vname = (('COVAXIN', 'Covaxin'),
                         ('COVISHIELD', 'CoviShield'),
                         ('sputnik', 'Sputnik'),)
    age_limit = ((18,'18+'),(45,'45+'))
    vtype = (('free','Free'),('paid','Paid'))
    age = models.IntegerField(default=None,choices=age_limit)
    vaccine_type = models.CharField(max_length=100,default=None, choices=vtype)
    vaccine_name = models.CharField(max_length=100,default=None, choices = vname)
    pincode = models.IntegerField(default=None)

    def __str__(self) -> str:
        return self.email
	
	
	
    






