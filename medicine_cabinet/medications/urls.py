from django.urls import path
from . import views

urlpatterns = [
    path('medications/', views.MedicationList.as_view()),
    path('medications/<int:pk>/', views.MedicationDetail.as_view())
]