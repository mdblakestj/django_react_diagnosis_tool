from django.db import models


class Symptom(models.Model):
    name = models.CharField(max_length=100)


class Diagnosis(models.Model):
    name = models.CharField(max_length=100)


class SymptomDiagnosis(models.Model):
    symptom = models.ForeignKey(Symptom, on_delete=models.DO_NOTHING)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.DO_NOTHING)
