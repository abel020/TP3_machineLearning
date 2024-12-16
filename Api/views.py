# views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import joblib
import numpy as np
import json  # Asegúrate de importar json

# Cargar el modelo al inicio
modelo_cargado = joblib.load('Api/modelo_knn_diabetes5050.pkl')

def formulario_view(request):
    return render(request, 'Prediccion.html')

class PredictAPIView(APIView):
    def post(self, request):
        return self.handle_request(request)

    def handle_request(self, request):
        try:
            # Obtener los datos de entrada
            data = json.loads(request.body)  # Para POST

            # Asegúrate de que el JSON tenga la estructura correcta
            features = data.get("features")

            if not features or not isinstance(features, list):
                return Response({"error": "No se enviaron datos válidos para la predicción."}, status=status.HTTP_400_BAD_REQUEST)

            # Convertir los datos al formato esperado por el modelo
            features = np.array(features).reshape(1, -1)  # Cambia el reshape si es necesario

            # Realizar la predicción
            prediction = modelo_cargado.predict(features)
            prediction_proba = modelo_cargado.predict_proba(features)

            # Devolver la respuesta en JSON
            return Response({
                "prediction": int(prediction[0]),
                "probabilities": prediction_proba[0].tolist()
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "error": str(e),
                "features": features  # Incluye los datos que se intentaron procesar
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Nuevas vistas
def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')

def Base(request):
    return render(request, 'base.html')

def info(request):
    return render(request, 'info.html')   

def diabetes(request):
    return render(request, 'diabetes.html')   

def sindiabetes(request):
    return render(request, 'sindiabetes.html')   

def prediabetes(request):
    return render(request, 'prediabetes.html')   

def about(request):
    return render(request, 'about.html')  


 