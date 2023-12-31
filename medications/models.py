# A Django model is a table in your database

from django.db import models
# from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

# Create your models here.
class Medication(models.Model):
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    medication_description = models.CharField(max_length=255, blank=True, null=True)
    pap_name = models.CharField(max_length=255, blank=True, null=True)
    pap_info_link = models.URLField(max_length=200, blank=True, null=True)
    pap_eligibility_link = models.URLField(max_length=200, blank=True, null=True)
    pap_application_link = models.URLField(max_length=200, blank=True, null=True)

# Converts Medication model instances to JSON representations (serialization)
class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ("id", "brand_name", "medication_description", "pap_name", "pap_info_link", "pap_eligibility_link", "pap_application_link")