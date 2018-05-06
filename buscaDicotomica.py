#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CÁLCULO DA FUNÇÃO NO PONTO X
f = (lambda x: x**2 + 2*x)

# ENCONTRANDO VALOR ÓTIMO COM A BUSCA DICOTÔMICA
def buscaDicotomica(a, b, delta, precisao):
	print("=" * 100)
	print("\nINÍCIO DA RESOLUÇÃO - BUSCA DICOTÔMICA\n")
	print("=" * 100)
	print("\n")
	k = 1
	while True:
		p = ((a + b)/2) - delta
		q = ((a + b)/2) + delta
		print(k,'|', a,'|', b,'|', p,'|', f(p),'|', q,'|', f(q),'|', b - a, '|')
		if ((b-a)<precisao):
			break
		if f(p)>f(q):
			a = p
		else:
			b = q
		k += 1

def main():
	a = float(input("Digite o valor de A: "))
	b = float(input("Digite o valor de B: "))
	delta = float(input("Digite o valor do delta: "))
	precisao = float(input("Digite o valor da precisao: "))
	buscaDicotomica(a, b, delta, precisao)
main()







