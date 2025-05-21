from django.urls import path
from . import views  # Ensure relative import to import views

urlpatterns = [
    path('', views.signature_form, name='signature_form'),
    path('signature-pad/', views.signature_pad, name='signature_pad'),
    path('submit-form/', views.submit_form, name='submit_form'),
    path('success/', views.success, name='success'),
]
