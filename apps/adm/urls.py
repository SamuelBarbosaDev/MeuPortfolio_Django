from django.urls import path
from . import views

urlpatterns = [
    path('portfólio/', views.portfólio, name='portfólio'),
    path('contato/', views.contato, name='contato'),
    path('', views.sobre, name='sobre'),
    path('portfólio/projeto/<int:id>/', views.projeto, name='projeto'),
]