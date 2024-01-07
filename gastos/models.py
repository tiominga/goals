from django.db import models
from categorias.models import Categoria

# Create your models here.
class Gasto(models.Model):
    obs = models.CharField(max_length=100)
    valor = models.FloatField()
    grupo = models.IntegerField()
    fk_categorias = models.ForeignKey(Categoria, on_delete = models.DO_NOTHING)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.obs