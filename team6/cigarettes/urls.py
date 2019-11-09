from django.urls import path
from . import views

app_name = 'cigarettes'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:cigarette_id>/',views.detail, name="detail"),
    path('like/<int:cigarrte_id>/',views.like, name="like"),
    path('<int:cigarette_id>/comment')
    path('newCigarette/', views.new_cigarette, name="new_cigarette"),
    path('newElecCigarette/', views.new_elec_cigarette, name="new_elec_cigarette"),
    path('createCigarette/', views.create_cigarette, name="create_cigarette"),
    path('createElecCigarette/', views.create_elec_cigarette, name="create_elec_cigarette"),
]