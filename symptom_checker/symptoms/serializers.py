from rest_framework import serializers
from symptoms.models import Diagnosis
from symptoms.models import Symptom
from symptoms.models import SymptomDiagnosis


class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ('id', 'name')


class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ('id', 'name')


class SymptomDiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SymptomDiagnosis
        fields = '__all__'

    def create(self, validated_data):
        return SymptomDiagnosis.objects.create(**validated_data)
