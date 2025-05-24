"""
URL configuration for lab_reservas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    UserCreate, UserDetail,
    ReservaCreate, ReservaDetail,
    LaboratorioReservas, ProfessorReservas
)

urlpatterns = [
    # Usuários
    path('usuarios/', UserCreate.as_view(), name='usuario-create'),
    path('usuarios/<int:pk>/', UserDetail.as_view(), name='usuario-detail'),
    
    # Reservas
    path('reservas/', ReservaCreate.as_view(), name='reserva-create'),
    path('reservas/<int:pk>/', ReservaDetail.as_view(), name='reserva-detail'),
    
    # Filtros
    path('laboratorios/<int:id>/reservas/', LaboratorioReservas.as_view(), name='laboratorio-reservas'),
    path('professores/<int:id>/reservas/', ProfessorReservas.as_view(), name='professor-reservas'),
]
