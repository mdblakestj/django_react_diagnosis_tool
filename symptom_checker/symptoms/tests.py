from django.test import TestCase
from symptoms.models import Symptom
from symptoms.models import Diagnosis
from symptoms.models import SymptomDiagnosis
from rest_framework.test import APITestCase


class SymptomTest(TestCase):
    """
    Creates Symptom and tests view

    """

    def create_symptom(self, name="Runny nose"):
        return Symptom.objects.create(name=name)

    def test_symptom_creation(self):
        w = self.create_symptom()
        self.assertTrue(isinstance(w, Symptom))
        self.assertEqual("Runny nose", w.name)

    def test_symptom_list_view(self):
        w = self.create_symptom()
        url = "/api/symptom/"
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.name, str(resp.content))

    def test_symptom_likely_view(self):
        url = "/api/symptom/3/likely/"
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)


class DiagnosisTest(TestCase):
    """
    Creates Diagnosis and tests view

    """

    def create_diagnosis(self, name="Common cold"):
        return Diagnosis.objects.create(name=name)

    def test_diagnosis_creation(self):
        w = self.create_diagnosis()
        self.assertTrue(isinstance(w, Diagnosis))
        self.assertEqual("Common cold", w.name)

    def test_diagnosis_list_view(self):
        w = self.create_diagnosis()
        url = "/api/diagnosis/"
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.name, str(resp.content))


class SymptomDiagnosisTest(TestCase):
    """
    Creates Diagnosis and tests view

    """

    def create_diagnosis(self, name="Common cold"):
        return Diagnosis.objects.create(name=name)

    def create_symptom(self, name="Runny nose"):
        return Symptom.objects.create(name=name)

    def create_symptomdiagnosis(self, symptom, diagnosis):
        return SymptomDiagnosis.objects.create(
            symptom=symptom, diagnosis=diagnosis
        )

    def test_symptomdiagnosis_creation(self):
        d = self.create_diagnosis()
        s = self.create_symptom()
        w = self.create_symptomdiagnosis(s, d)
        self.assertTrue(isinstance(w, SymptomDiagnosis))


class TestSymptomApi(APITestCase):
    """
    Tests Symptom API endpoint with POST and GET

    """

    def setUp(self):
        # create symptom
        self.symptom = Symptom(name="Runny Nose")
        self.symptom.save()

    def test_symptom_creation(self):
        response = self.client.post(
            "/api/symptom/", {"name": "Runny Nose"}
        )

        # assert new symptom was added
        self.assertEqual(Symptom.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    def test_getting_symptoms(self):
        response = self.client.get(
            "/api/symptom/", format="json"
        )
        self.assertEqual(len(response.data), 1)


class TestDiagnosisApi(APITestCase):
    """
    Tests Diagnosis API endpoint with POST and GET

    """

    def setUp(self):
        # create diagnosis
        self.diagnosis = Diagnosis(name="Hives")
        self.diagnosis.save()

    def test_symptom_creation(self):
        response = self.client.post(
            "/api/diagnosis/", {"name": "Hives"}
        )

        # assert new diagnosis was added
        self.assertEqual(Diagnosis.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    def test_getting_symptoms(self):
        response = self.client.get(
            "/api/diagnosis/", format="json"
        )
        self.assertEqual(len(response.data), 1)


class TestSymptomDiagnosisApi(APITestCase):
    """
    Tests SymptomDiagnosis API endpoint with POST and GET

    """

    def setUp(self):
        # create diagnosis
        self.symptom = Symptom(name="Runny Nose")
        self.symptom.save()
        self.diagnosis = Diagnosis(name="Hives")
        self.diagnosis.save()
        self.symptom.save()
        self.symptomdiagnosis = SymptomDiagnosis(
            symptom=self.symptom, diagnosis=self.diagnosis
        )
        self.symptomdiagnosis.save()

    def test_symptomdiagnosis_creation(self):
        response = self.client.post(
            "/api/symptomdiagnosis/",
            {
                "symptom": self.symptom.id,
                "diagnosis": self.diagnosis.id,
            },
            format="json",
        )

        # assert new symptomdiagnosis was added
        self.assertEqual(
            SymptomDiagnosis.objects.count(), 2
        )

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    def test_symptomdiagnosislikely_get(self):
        self.url = (
            "/api/symptom/"
            + str(self.symptom.id)
            + "/likely/"
        )
        response = self.client.get(self.url, format="json")

        self.assertEqual(len(response.data), 1)
        self.assertEqual(200, response.status_code)
        # test likely logic
        self.assertEqual(
            response.data,
            [
                {
                    "diagnosis_id": self.diagnosis.id,
                    "id__count": 1,
                }
            ],
        )

    def test_getting_symptoms(self):
        response = self.client.get(
            "/api/symptomdiagnosis/", format="json"
        )
        self.assertEqual(len(response.data), 1)
