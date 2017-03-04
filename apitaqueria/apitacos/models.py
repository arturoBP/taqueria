from django.db import models

# Create your models here.


CALIF = (
		('EX','5'),#opciones que podemos estar eligiendo
		('BU','4'),
		('RE','3'),
		('MA','2'),
		('MM','1'),
)

class TacosModel(models.Model):
	id = models.AutoField(primary_key=True)
	nombretaqueria = models.CharField(max_length=50)
	latitud = models.FloatField()
	longitud = models.FloatField()
	calificacion = models.CharField(choices=CALIF,max_length=50, null=True, blank=True)
	imagen = models.URLField(max_length=200)

def _str_(self): 
	return self.nombretaqueria