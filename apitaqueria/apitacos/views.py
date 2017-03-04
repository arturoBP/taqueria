from django.shortcuts import render
from apitacos.models import TacosModel
from rest_framework import generics
from rest_framework.response import *
from apitacos.serializers import Tacosserializer





# Create your views here.
class TacosList(generics.ListCreateAPIView):
	queryset = TacosModel.objects.all()
	serializer_class = Tacosserializer


		#return self.list(self,request)

class Tacosdetalle(generics.RetrieveUpdateDestroyAPIView):

    queryset = TacosModel.objects.all()
    serializer_class = Tacosserializer

# Create your views here.
