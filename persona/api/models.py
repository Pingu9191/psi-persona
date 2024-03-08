from django.db import models

# Create your models here.

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
    class Meta:
        ordering = ['id']
        db_table = 'auth_user'