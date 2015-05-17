from django.db import models
from django.contrib.auth.models import User
from datetime import datetime    

# Create your models here.

class Personal(models.Model):
	usuario = models.OneToOneField(User)
	nombre = models.CharField(max_length=50, blank=True)
	apellidop = models.CharField(max_length=50, blank=True)
	apellidom = models.CharField(max_length=50, blank=True)
	clavepresupuestal = models.CharField(max_length=50, blank=True)
	telefono = models.CharField(max_length=13, blank=True)
	direccion = models.CharField(max_length=80, blank=True)
	correo = models.CharField(max_length=20, blank=True)
	curp = models.CharField(max_length=50, blank=True)
	aingresep = models.CharField(max_length=6, blank=True)
	aingreescuela = models.CharField(max_length=6, blank=True)
	aingrezona = models.CharField(max_length=6, blank=True)
	fechanacimiento = models.DateField(blank=True, null=True)
	rfc = models.CharField(max_length=50, blank=True)
	cargo = models.CharField(max_length=50, blank=True)
	
	def __unicode__(self):
		return self.rfc

class Tutor(models.Model):
	nombreT = models.CharField(max_length=50, blank=True)
	apellidoPt = models.CharField(max_length=50, blank=True)
	apellidoMt= models.CharField(max_length=50, blank=True)
	ocupacion= models.CharField(max_length=50, blank=True)
	direccion= models.CharField(max_length=50, blank=True)
	telefonoCasa= models.CharField(max_length=50, blank=True)
	telefonoCel= models.CharField(max_length=50, blank=True)
	idT= models.CharField(max_length=50, blank=True)
	def __unicode__(self):
		return self.idT


class Grupo(models.Model):
	gradogrupo = models.CharField(max_length=10, blank=True) #se ingresa  2 A , 3C, ETC
	idprofesor = models.ForeignKey(Personal)
	def __unicode__(self):
		return self.gradogrupo

class Alumno(models.Model):
	usuario = models.OneToOneField(User)
	nombrea = models.CharField(max_length=50, blank=True)
	apellidoPa = models.CharField(max_length=50, blank=True)
	apellidoMa= models.CharField(max_length=50, blank=True)
	sexo = models.CharField(max_length=15, blank=True)
	correo = models.CharField(max_length=30, blank=True)
	curp = models.CharField(max_length=45, blank=True)
	fechanacimiento = models.DateField(blank=True, null=True)
	rh = models.CharField(max_length=50, blank=True) #tipo sangre
	tutor1= models.ForeignKey(Tutor)
	idgrupo = models.ForeignKey(Grupo)
	def __unicode__(self):
		return unicode(self.apellidoPa)+ ' ' + str(self.apellidoMa)+ ' ' + str(self.nombrea)+ ' ' + str(self.curp)


class Escuela(models.Model):
	clave= models.CharField(max_length=12, blank=True)
	nombre=  models.CharField(max_length=50, blank=True)
	zona = models.CharField(max_length=50, blank=True)
	turno=  models.CharField(max_length=12, blank=True)
	direccion = models.CharField(max_length=50, blank=True)
	telefono = models.CharField(max_length=15, blank=True)
	correo = models.CharField(max_length=50, blank=True)
	paginaweb = models.CharField(max_length=50, blank=True)

	def __unicode__(self):
		return unicode(self.nombre)+ ' ' + str(self.turno)+ ' ' + str(self.clave)


class Boleta1(models.Model):
	codigoboleta = models.CharField(max_length=50, blank=True)
	idprofesor=  models.ForeignKey(Personal)
	idgrupo =  models.ForeignKey(Grupo)
	idalumno = models.ForeignKey(Alumno)
	idescuela = models.ForeignKey(Escuela)
	cicloescolar = models.CharField(max_length=50, blank=True, null=True)
	fechadevalidacion = models.DateField(default=datetime.now, blank=True, null=True, )
	lugardevalidacion =models.CharField(default="-", max_length=50, blank=True, null=True)
	promovido = models.BooleanField(default=False)
	promedio = models.DecimalField(max_digits = 2, decimal_places = 1,default=0.0, blank=True, null=True)
	inasistencias1= models.IntegerField(default=0, blank=True, null=True)
	inasistencias2= models.IntegerField(default=0, blank=True, null=True)
	inasistencias3= models.IntegerField(default=0, blank=True, null=True)
	inasistencias4= models.IntegerField(default=0, blank=True, null=True)
	inasistencias5= models.IntegerField(default=0, blank=True, null=True)
	inasistenciastotal= models.IntegerField(default=0, blank=True, null=True)
	espanol1 = models.IntegerField(default=0, blank=True, null=True)
	espanol2 = models.IntegerField(default=0, blank=True, null=True)
	espanol3 = models.IntegerField(default=0, blank=True, null=True)
	espanol4 = models.IntegerField(default=0, blank=True, null=True)
	espanol5 = models.IntegerField(default=0, blank=True, null=True)
	espanolpromedio = models.IntegerField(default=0, blank=True, null=True)
	matematicas1 = models.IntegerField(default=0, blank=True, null=True)
	matematicas2 = models.IntegerField(default=0, blank=True, null=True)
	matematicas3 = models.IntegerField(default=0, blank=True, null=True)
	matematicas4 = models.IntegerField(default=0, blank=True, null=True)
	matematicas5 = models.IntegerField(default=0, blank=True, null=True)
	matematicaspromedio = models.IntegerField(default=0, blank=True, null=True)
	exploracion1 = models.IntegerField(default=0, blank=True, null=True)
	exploracion2 = models.IntegerField(default=0, blank=True, null=True)
	exploracion3 = models.IntegerField(default=0, blank=True, null=True)
	exploracion4 = models.IntegerField(default=0, blank=True, null=True)
	exploracion5 = models.IntegerField(default=0, blank=True, null=True)
	exploracionpromedio = models.IntegerField(default=0, blank=True, null=True)
	formacion1 = models.IntegerField(default=0, blank=True, null=True)
	formacion2 = models.IntegerField(default=0, blank=True, null=True)
	formacion3 = models.IntegerField(default=0, blank=True, null=True)
	formacion4 = models.IntegerField(default=0, blank=True, null=True)
	formacion5 = models.IntegerField(default=0, blank=True, null=True)
	formacionpromedio = models.IntegerField(default=0, blank=True, null=True)
	fisica1 = models.IntegerField(default=0, blank=True, null=True)
	fisica2 = models.IntegerField(default=0, blank=True, null=True)
	fisica3 = models.IntegerField(default=0, blank=True, null=True)
	fisica4 = models.IntegerField(default=0, blank=True, null=True)
	fisica5 = models.IntegerField(default=0, blank=True, null=True)
	fisicapromedio = models.IntegerField(default=0, blank=True, null=True)
	artistica1 = models.IntegerField(default=0, blank=True, null=True)
	artistica2 = models.IntegerField(default=0, blank=True, null=True)
	artistica3 = models.IntegerField(default=0, blank=True, null=True)
	artistica4 = models.IntegerField(default=0, blank=True, null=True)
	artistica5 = models.IntegerField(default=0, blank=True, null=True)
	artisticapromedio = models.IntegerField(default=0, blank=True, null=True)
	aviso1 = models.BooleanField(default=False)
	aviso2 = models.BooleanField(default=False)
	aviso3 = models.BooleanField(default=False)

	def __unicode__(self):
		return self.codigoboleta




class Tarea(models.Model):
	idgrupo=  models.ForeignKey(Grupo)
	tarea = models.TextField(max_length=200, blank=True)	
	#def __unicode__(self):
	#	return self.idgrupo

class Consejo(models.Model):
	director=  models.ForeignKey(Personal)
	#profesor=  models.ForeignKey(Personal)
	