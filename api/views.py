from rest_framework import viewsets

from api.models import Event, Person, Usuario, Transaccion
from api.serializers import EventSerializer, PersonSerializer, UsuarioSerializer, TransaccionSerializer


class EventViewSet(viewsets.ModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer

class PersonViewSet(viewsets.ModelViewSet):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer

class TransaccionViewSet(viewsets.ModelViewSet):
	queryset = Transaccion.objects.all()
	serializer_class = TransaccionSerializer
