# vistes de la app

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'), # pagina principal
    path('<str:num>', views.num, name='num'), # pagina que mostra el dia de la setmana segons el número
]
