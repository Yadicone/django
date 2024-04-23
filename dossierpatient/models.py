from django.db import models


class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_de_naissance = models.DateField()
    sexe = models.CharField(max_length=1, choices=(('M', 'Masculin'), ('F', 'Féminin')))
    adresse = models.CharField(max_length=255)
    

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Praticien(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class CentreDeSante(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    

    def __str__(self):
        return self.nom

