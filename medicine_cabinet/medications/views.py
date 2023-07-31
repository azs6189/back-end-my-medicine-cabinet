from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParse
from medications.models import Medication, MedicationSerializer
# from django.template import loader

# Create your views here.
# def medications(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())

class MedicationList(APIView):
    def get(self, request):
        medications = Medication.objects.all()
        serializer = MedicationSerializer(medications, many=True)
        return JsonResponse(serializer.data, safe=False)