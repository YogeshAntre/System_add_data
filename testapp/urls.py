from django.urls import path
from testapp.views import DataDisplay
urlpatterns = [
    path('data/',DataDisplay.as_view()),
    path('mymodel/<int:pk>/', MyModelRetrieveView.as_view(), name='mymodel-detail'),
]