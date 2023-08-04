from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from medications.models import Medication, MedicationSerializer
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
import psycopg2 #directly being used to interact with the PostgreSQL database in the MedicationList and MedicationDetail views to retrieve, create, update, and delete medication instances

# from django.template import loader

# Create your views here.
# def medications(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())

class MedicationList(APIView):
    """
    List all medications, or create a new medication
    """
    def get(self, request, format=None):
        medications = Medication.objects.all()
        serializer = MedicationSerializer(medications, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        # data = JSONParser().parse(request)
        serializer = MedicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicationDetail(APIView):
    """
    Retrieve, update or delete a medication instance
    """

    def get_object(self, pk):
        try:
            return Medication.objects.get(pk=pk)
        except Medication.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        medication = self.get_object(pk)
        serializer = MedicationSerializer(medication)
        return Response(serializer.data, status = 201)
    
    def put(self, request, pk):
        medication = self.get_object(pk)
        serializer = MedicationSerializer(medication, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)
    
    def delete(self, request, pk):
        medication = self.get_object(pk)
        medication.delete()
        return Response(status = 204)