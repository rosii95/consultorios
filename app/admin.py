from django.contrib import admin
from .models import doc,turno,esp,pacientes,obras_sociales, enfermedad, consultorios

class doctoresAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','especialidad','consultorio')
    search_fields=('nombre','apellido','especialidad',)
    
class pacientesAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','enfermedad')
    search_fields=('nombre','apellido',)
    
class turnoAdmin(admin.ModelAdmin):
    list_display=('fecha','hora','paciente','doctor', 'especialidad')

class osAdmin(admin.ModelAdmin):
    list_display=('id','nombre','detalle')

class enfermedadAdmin(admin.ModelAdmin):
    list_display=('id','descripción')

class consultoriosAdmin(admin.ModelAdmin):
    list_display=('id','detalle')

admin.site.register(doc,doctoresAdmin)
admin.site.register(turno,turnoAdmin)
admin.site.register(esp)
admin.site.register(enfermedad,enfermedadAdmin)
admin.site.register(pacientes,pacientesAdmin)
admin.site.register(obras_sociales, osAdmin)
admin.site.register(consultorios, consultoriosAdmin)