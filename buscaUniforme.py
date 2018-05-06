#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CÁLCULO DA FUNÇÃO NO PONTO X
f = (lambda x: x**2 + 2*x)

# ENCONTRANDO VALOR ÓTIMO COM A BUSCA UNIFORME
def buscaUniforme(a, b, delta):
	print("=" * 100)
	print("\nINÍCIO DA RESOLUÇÃO - BUSCA UNIFORME\n")
	print("=" * 100)
	print("\n")
	p = a
	numeroAumentos = 0
	listaP = []
	listaFQ = []
	for k in range(1,100):
		if p > b:
			break
		q = p + delta
		print(k,'|', p,'|', f(p),'|', q,'|', f(q),'|')
		print('-' * 40)
		listaP.append(p)
		listaFQ.append(f(q))
		if listaFQ[len(listaFQ) - 1] > listaFQ[len(listaFQ) - 2]:
			numeroAumentos += 1
			if numeroAumentos == 2:
				break
			print("AUMENTOU")
			print('-' * 40)
			p = listaP[len(listaP) - 2]
			delta /= 10 
		else:
			p = q

def main():
	a = float(input("Digite o valor de A: "))
	b = float(input("Digite o valor de B: "))
	delta = float(input("Digite o valor do delta: "))
	buscaUniforme(a, b, delta)
main()
