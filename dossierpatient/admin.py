from django.contrib import admin
from .models import Patient, Praticien, CentreDeSante

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'date_de_naissance', 'sexe', 'adresse']
    # Ajoutez d'autres configurations d'administration pour le modèle Patient

@admin.register(Praticien)
class PraticienAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'specialite']
    # Ajoutez d'autres configurations d'administration pour le modèle Praticien

@admin.register(CentreDeSante)
class CentreDeSanteAdmin(admin.ModelAdmin):
    list_display = ['nom', 'adresse']
    # Ajoutez d'autres configurations d'administration pour le modèle CentreDeSante




