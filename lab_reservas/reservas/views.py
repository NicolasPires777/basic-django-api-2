from rest_framework import generics
from .models import User, Reserva
from .serializers import UserSerializer, ReservaSerializer

# Endpoints para Usuários
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Endpoints para Reservas
class ReservaCreate(generics.CreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaDetail(generics.RetrieveAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

# Filtros por Laboratório e Professor
class LaboratorioReservas(generics.ListAPIView):
    serializer_class = ReservaSerializer
    def get_queryset(self):
        lab_id = self.kwargs['id']
        return Reserva.objects.filter(laboratorio_id=lab_id)

class ProfessorReservas(generics.ListAPIView):
    serializer_class = ReservaSerializer
    def get_queryset(self):
        professor_id = self.kwargs['id']
        return Reserva.objects.filter(professor_id=professor_id)