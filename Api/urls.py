# Api/urls.py
from django.urls import path
from .views import PredictAPIView, formulario_view

urlpatterns = [
    path('predict/', PredictAPIView.as_view(), name="predict"),
    path('formulario/', formulario_view, name="formulario"),
    
]