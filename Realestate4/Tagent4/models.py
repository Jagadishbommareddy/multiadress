from django.core.urlresolvers import reverse
from django.db import models
from .validations import *
class Agent(models.Model):
    agent_id= models.AutoField(primary_key=True)
    first_name= models.CharField(max_length=20,validators=[validate_first_name])
    last_name= models.CharField(max_length=20,validators=[validate_last_name])
    age=models.IntegerField()
    education= models.CharField(max_length=50,validators=[validate_education])
    company_name=models.CharField(max_length=50)
    specialization= models.CharField(max_length=100,validators=[validate_specelization])
    experence=models.IntegerField()
    agent_notes=models.TextField()
def get_absolute_url(self):
        return reverse('agent-update', kwargs={'pk': self.pk})
class Address(models.Model):
    agent= models.ForeignKey(Agent)
    address_id= models.AutoField(primary_key=True)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=20,validators=[validate_city])
    state= models.CharField(max_length=20,validators=[validate_state])
    landmark= models.CharField(max_length=20,validators=[validate_landmark])
    pincode= models.IntegerField()

