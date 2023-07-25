from django.urls import path
from . import views

urlpatterns = [
    path('medications/', views.medications, name='medications')
]