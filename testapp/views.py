from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import ToDoSerializers,ToDo
# Create your views here.
class DataDisplay(ListCreateAPIView):
    serializer_class=ToDoSerializers
    queryset=ToDo.objects.all()
    
