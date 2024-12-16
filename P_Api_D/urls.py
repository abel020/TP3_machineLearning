from django.contrib import admin
from django.urls import path, include
from Api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Api.urls')),
    path('', views.index, name='home'),  # Redirige la ruta principal a index
    path('index', views.index, name='index'),  # Puedes mantener esta ruta como alias si es necesario
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('info/', views.info, name='info'),
    path('diabetes/', views.diabetes, name='diabetes'),
    path('sindiabetes/', views.sindiabetes, name='sindiabetes'),
    path('about/', views.about, name='about'),
    
    path('prediabetes/', views.prediabetes, name='prediabetes'),
]
