from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('turnos/', views.turnos, name='turnos'),
    path('turnos/eliminar_turno/<int:id>',views.eliminar_turno),
    path('doctores/', views.doctores, name='doctores'),
    path('consultorios/', views.consultorios, name='consultorios'),
]