from django.shortcuts import render
from django.http import JsonResponse
from .models import Patient


def index(request):
    return render(request,'index.html')

# gestionpatient/views.py


def liste_patients(request):
    patients = Patient.objects.all()
    return render(request, 'template.html', {'patients': patients})
    # ou pour une réponse JSON
    # return JsonResponse({'patients': list(patients.values())})
