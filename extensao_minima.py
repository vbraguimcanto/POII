import numpy as np
from random import randint

def verificaMenorCaminho(visitado, vetorDistancias):
	for i in range(0,len(visitado)):
		menorValor = min(vetorDistancias[visitado][i])
		indice = i
		if i != 0:
			if(menorValorAtual < menorValor):
				menorValorAtual = menorValor
				indice = i
		else:
			menorValorAtual = menorValor
			indice = i

	return indice


def buscaExtensaoMinima(vetorCidades, vetorDistancias, noInicial):
	visitado = []
	visitado.append(noInicial)
	nosVisitados = 0
	while(nosVisitados < len(vetorCidades)):
		visitado.append(verificaMenorCaminho(visitado), vetorDistancias)

def main():
	vetorCidades = ['Bauru', 'Campinas', 'Sorocaba', 'SJRP', 'RP']
	vetorDistancias = np.array([[10000000000, 80, 100, 75, 80], [80, 10000000000, 60, 35, 45], [100, 60, 10000000000, 25, 100], [75, 35, 25, 10000000000, 55], [80, 45, 100, 55, 10000000000]])
	noInicial = randint(0,len(vetorCidades) - 1)
	buscaExtensaoMinima(vetorCidades, vetorDistancias, noInicial)

main()