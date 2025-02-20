from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import ToDoSerializers,ToDo
# Create your views here.
class DataDisplay(ListCreateAPIView):
    serializer_class=ToDoSerializers
    queryset=ToDo.objects.all()


from rest_framework.generics import RetrieveAPIView
from myapp.models import MyModel
from myapp.serializers import MyModelSerializer

class MyModelRetrieveView(RetrieveAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    
