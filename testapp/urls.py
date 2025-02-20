from django.urls import path
from testapp.views import DataDisplay
urlpatterns = [
    path('data/',DataDisplay.as_view())
]