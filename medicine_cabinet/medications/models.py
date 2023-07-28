# A Django model is a table in your database

from django.db import models

# Create your models here.
class Medication(models.Model):
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    medication_description = models.CharField(max_length=255, blank=True, null=True)
    pap_name = models.CharField(max_length=255, blank=True, null=True)
    pap_info_link = models.URLField(max_length=200, blank=True, null=True)
    pap_eligibility_link = models.URLField(max_length=200, blank=True, null=True)
    pap_application_link = models.URLField(max_length=200, blank=True, null=True)
