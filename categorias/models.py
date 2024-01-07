from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=60)
    meta = models.FloatField()
    status = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nome

