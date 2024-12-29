from django.db import models

class Citacao(models.Model):
    texto = models.TextField()
    autor = models.CharField(max_length=100)

    def __str__(self):
        return f'"{self.texto}" - {self.autor}'
