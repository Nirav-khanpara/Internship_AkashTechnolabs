from django.urls import path
from . import views

urlpatterns = [
    path('myform/', views.form, name='form'),
    path('myform/formprocess/', views.process, name='formprocess'),

]