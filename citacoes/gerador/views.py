from django.shortcuts import render

from .models import Citacao
import random

def exibir_citacao(request):
    # Seleciona uma citação aleatória
    citacoes = Citacao.objects.all()
    citacao = random.choice(citacoes) if citacoes else None
    return render(request, 'gerador/citacoes.html', {'citacao': citacao})
