from django.db import models

class esp(models.Model):
    nombre=models.CharField(max_length=30, null=False, verbose_name='nombre')
    def __str__(self):
        return '%s'%(self.nombre) 
    class Meta:
        db_table = 'esp'
        verbose_name = 'especialización'
        verbose_name_plural = 'especialidades'

class doctores(models.Model):
    MP=models.PositiveIntegerField()
    nombre=models.CharField(max_length=30, null=False, verbose_name='nombre')
    apellido=models.CharField(max_length=30, null=False, verbose_name='apellido')
    especialidad=models.ForeignKey(esp, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return '%s  %s'%(self.nombre,self.apellido)  
    class Meta:
        db_table = 'doctores'
        verbose_name = 'doctor'
        verbose_name_plural = 'doctores'
        
        
class obras_sociales(models.Model):
    nombre=models.CharField(max_length=30, null=False, verbose_name='nombre')
    detalle=models.CharField(max_length=100, null=False, verbose_name='detalle')
    def __str__(self):
        return '%s'%(self.nombre)  
    class Meta:
        db_table = 'os'
        verbose_name = 'os'
        verbose_name_plural = 'obras socialas'

class pacientes(models.Model):
    dni=models.CharField(max_length=8, null=False, verbose_name='DNI')
    nombre=models.CharField(max_length=30, null=False, verbose_name='Nombre')
    apellido=models.CharField(max_length=30, null=False, verbose_name='Apellido')
    obra_social=models.ForeignKey(obras_sociales, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return '%s  %s'%(self.nombre,self.apellido)  
    class Meta:
        db_table = 'pacientes'
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'
        
class turno(models.Model):
    fecha=models.DateField()
    hora=models.TimeField()
    doctor=models.ForeignKey(doctores, on_delete=models.CASCADE, blank=True, null=True)
    paciente=models.ForeignKey(pacientes, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return '%s  %s'%(self.fecha,self.hora)  
    class Meta:
        db_table = 'turno'
        verbose_name = 'turno'
        verbose_name_plural = 'turno'
