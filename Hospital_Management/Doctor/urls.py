from django.urls import path
from . import views


urlpatterns =[
    path("doc-dashbord/", views.doc_dashbord),
    path("doc-reg/", views.Doc_reg),
    path('prescription-form/', views.prescription_form),
    path('patient-history/', views.patient_history),
    
]