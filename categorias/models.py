from django.db import models

class Categoria(models.Model):
    categ = models.CharField(max_length=100)
    def __str__(self):
        return self.categ
