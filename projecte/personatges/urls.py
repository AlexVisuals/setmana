'''
Fitxer que creem nosaltres per posar les vistes de l'app
'''
from django.urls import path
from . import views

urlpatterns=[ # Aquí defineixo les rutes de les URLs
  path('', views.home, name='home'),
  path("<str:opcio>/", views.personatge, name="personatge"),
]