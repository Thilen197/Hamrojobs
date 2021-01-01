from django.db import models

# Create your models here.
#Charfield=varchar
#Floatfield=Float
#IntegerField=Integers

class Jobs(models.Model):
    job_name = models.CharField(max_length=50)
    job_address = models.CharField(max_length=50)
    contact_number = models.FloatField(max_length=15)
    jobs_description = models.CharField(max_length=200)
    user_id = models.IntegerField()