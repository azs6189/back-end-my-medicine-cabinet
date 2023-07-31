from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from medications.models import Medication, MedicationSerializer
# from django.template import loader

# Create your views here.
# def medications(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())

class MedicationList(APIView):
    """
    List all medications, or create a new medication
    """
    def get(self, request):
        medications = Medication.objects.all()
        serializer = MedicationSerializer(medications, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = MedicationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
    