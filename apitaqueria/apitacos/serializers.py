from rest_framework import serializers
from apitacos.models import TacosModel



class Tacosserializer(serializers.ModelSerializer):

	class Meta:

		model = TacosModel
		fields = ('nombretaqueria','latitud','longitud','calificacion','imagen')