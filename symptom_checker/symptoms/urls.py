from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('symptom', views.SymptomView)
router.register('diagnosis', views.DiagnosisView)
router.register('symptomdiagnosis', views.SymptomDiagnosisView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]
