from rest_framework import serializers
from .models import User, Professor, Laboratorio, Reserva

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorio
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nome', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'nome', 'matricula', 'especialidade']

class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorio
        fields = ['id', 'nome', 'local', 'capacidade']

class ReservaSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    professor = ProfessorSerializer(read_only=True)
    laboratorio = LaboratorioSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    professor_id = serializers.PrimaryKeyRelatedField(queryset=Professor.objects.all(), write_only=True)
    laboratorio_id = serializers.PrimaryKeyRelatedField(queryset=Laboratorio.objects.all(), write_only=True)

    class Meta:
        model = Reserva
        fields = [
            'id', 'data_reserva', 'hora_inicio', 'hora_fim',
            'user', 'professor', 'laboratorio',
            'user_id', 'professor_id', 'laboratorio_id'
        ]

    def validate(self, data):
        if data['hora_inicio'] >= data['hora_fim']:
            raise serializers.ValidationError("A hora de início deve ser antes da hora de fim.")
        
        # Verifica conflitos de reserva
        conflitos = Reserva.objects.filter(
            data_reserva=data['data_reserva'],
            laboratorio=data['laboratorio_id'],
        ).exclude(
            hora_fim__lte=data['hora_inicio'],
        ).exclude(
            hora_inicio__gte=data['hora_fim'],
        )
        if conflitos.exists():
            raise serializers.ValidationError("Conflito de horário para este laboratório.")
        return data

    def create(self, validated_data):
        # Mapeia IDs para objetos
        validated_data['user'] = validated_data.pop('user_id')
        validated_data['professor'] = validated_data.pop('professor_id')
        validated_data['laboratorio'] = validated_data.pop('laboratorio_id')
        return super().create(validated_data)