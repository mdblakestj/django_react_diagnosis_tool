from django.db.models import Count
from symptoms.models import Symptom, Diagnosis, SymptomDiagnosis
from symptoms.serializers import (
    SymptomSerializer,
    DiagnosisSerializer,
    SymptomDiagnosisSerializer
)
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class SymptomView(viewsets.ModelViewSet):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

    @action(detail=True, methods=['get'], name="likely", url_path='likely')
    def likely(self, request, pk):
        data = [
            x for x in SymptomDiagnosis.objects.filter(
                symptom_id=pk
            ).values('diagnosis_id').annotate(Count('id')).all()
        ]

        return Response(data)
        # return Response({"ok": pk})


class DiagnosisView(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer


class SymptomDiagnosisView(viewsets.ModelViewSet):
    queryset = SymptomDiagnosis.objects.all()
    serializer_class = SymptomDiagnosisSerializer
