from django.urls import path     
from . import views

urlpatterns = [
    path('', views.show),
    path('take',views.take),
    path('delete',views.delete),	   
]