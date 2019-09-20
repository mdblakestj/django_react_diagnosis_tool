# A Simple Diagnosing Tool Coding Challenge

This is a simple diagnosing tool built with Django and React.

## Installation

Install node packages:

```
npm install
```

Install Python packages:

pip install -r requirements.txt

## Deployment

Populate database with fixtures:

```
$ python manage.py loaddata symptomdiagnosis
$ python manage.py loaddata symptom
$ python manage.py loaddata diagnosis

```

Django server can be launched locally from command line:

```
$ python manage.py runserver
```

Launch webpack:

```
$ python manage.py runserver
```

Access app at http://127.0.0.1:8000/

# APIs

## Symptoms

Returns symptom names and ids

### Request

`GET /api/symptom/`

### Example response:

```
Response: [
    {
        "id": 1,
        "name": "sore throat"
    },
    {
        "id": 2,
        "name": "itchy rash"
    },
    {
        "id": 3,
        "name": "runny nose"
    }
]

```

## Diagnoses

Returns diagnoses names and ids

### Request

`GET /api/diagnosis/`

### Example response:

```
Response: [
    {
        "id": 1,
        "name": "common cold"
    },
    {
        "id": 2,
        "name": "viral throat infection"
    }
]

```

## Symptom Diagnosis Join Table

Returns symptom diagnosis occurrences

### Request

`GET /api/symptomdiagnosis/`

### Example response:

```
Response: [
    {
        "id": 1,
        "symptom": 1,
        "diagnosis": 1
    },
    {
        "id": 2,
        "symptom": 1,
        "diagnosis": 2
    },
    {
        "id": 3,
        "symptom": 1,
        "diagnosis": 3
    }
]

```

## Symptom Diagnosis Likely

Returns a count of diagnosis instances for each symptom

### Request

`GET /api/symptom/{symptom_id}/likely`

### Example response:

```
Response: [
    {
        "diagnosis_id": 1,
        "id__count": 1
    },
    {
        "diagnosis_id": 7,
        "id__count": 1
    }
]

```

## Symptom Diagnosis Occurrence POST

Posts a symptom diagnosis occurrence

### Request

`POST /api/symptomdiagnosis`

### Example body:

```
body = {
        "symptom": 1,
        "diagnosis": 1
    }
```

## Tests

To run tests:

```
python3 manage.py test
```
# django_react_diagnosis_tool
