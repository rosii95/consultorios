from django.contrib import admin
from .models import doctores,turno,esp,pacientes,obras_sociales

class doctoresAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','especialidad',)
    search_fields=('nombre','apellido','especialidad',)
    
class pacientesAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido',)
    search_fields=('nombre','apellido',)
    
class turnoAdmin(admin.ModelAdmin):
    list_display=('fecha','hora','paciente',)

admin.site.register(doctores,doctoresAdmin)
admin.site.register(turno,turnoAdmin)
admin.site.register(esp)
admin.site.register(pacientes,pacientesAdmin)
admin.site.register(obras_sociales)