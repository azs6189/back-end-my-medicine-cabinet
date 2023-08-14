from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from medications.models import Medication, MedicationSerializer
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .models import Medication

class MedicationList(APIView):
    """
    List all medications, or create a new medication
    """
    def get(self, request, format=None):
        medications = Medication.objects.all()
        serializer = MedicationSerializer(medications, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request, format=None):
        # data = JSONParser().parse(request)
        serializer = MedicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        return JsonResponse(serializer.data, status = 201)
    
    def put(self, request, pk):
        medication = self.get_object(pk)
        serializer = MedicationSerializer(medication, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
    
    def delete(self, request, pk):
        medication = self.get_object(pk)
        medication.delete()
        return JsonResponse(status = 204)
    
class SearchMedications(APIView):
    def get(self, request):
        brand_name = request.query_params.get('brand_name', None)

        if brand_name:
            medications = Medication.objects.filter(brand_name__icontains=brand_name)
            serializer = MedicationSerializer(medications, many=True)
            return Response(serializer.data)
        else:
            return Response("No medications found", status=status.HTTP_404_NOT_FOUND)