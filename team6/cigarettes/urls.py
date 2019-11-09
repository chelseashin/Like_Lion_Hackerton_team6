from django.urls import path
from . import views

app_name = 'cigarettes'

urlpatterns = [
    path('', views.index, name="index"),
]