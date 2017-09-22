from rest_framework import serializers

from api.models import Event, Person, Usuario, Transaccion


class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = "__all__"

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = "__all__"

class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Usuario
		fields = "__all__"

class TransaccionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaccion
		fields = "__all__"
