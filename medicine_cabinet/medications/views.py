from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def medications(request):
    return HttpResponse("Hello World")
