from django.db import models

# ==========================================
# MODELO: Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: Transporte
class Transporte(models.Model):
    nombre_transporte = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    capacidad = models.PositiveIntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    horario = models.TimeField(blank=True, null=True)
    empresa = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.nombre_transporte

# ==========================================
# MODELO: Viaje
class Viaje(models.Model):
    nombre_viaje = models.CharField(max_length=150)
    destino = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    fecha_salida = models.DateField(blank=True, null=True)
    fecha_regreso = models.DateField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    transporte = models.ForeignKey(
        Transporte,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='viajes'
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='viajes'
    )

    def __str__(self):
        return f"{self.nombre_viaje} - {self.destino}"
