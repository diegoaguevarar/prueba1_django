from __future__ import unicode_literals
from django.db import models

class Person(models.Model):
	name = models.CharField(max_length=30, blank=False)
	email = models.EmailField(unique=True, blank=False)
	def __str__(self):
		return self.email

class Event(models.Model):
	name = models.CharField(max_length=50)
	location = models.CharField(max_length=100)
	host = models.ForeignKey(Person, on_delete=models.CASCADE, to_field="email")
	def __str__(self):
		return self.name

class Usuario(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	gmail = models.EmailField(unique=True, blank=False)
	def __str__(self):
		return self.gmail

class Transaccion(models.Model):
	user= models.ForeignKey(Usuario, on_delete=models.CASCADE)
	cantidad = models.IntegerField()
	date = models.DateField()
	def __str__(self):
		return self.user
