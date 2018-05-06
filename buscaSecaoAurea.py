#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CÁLCULO DA FUNÇÃO NO PONTO X
f = (lambda x: x**2 - 2*x + 3)

# ENCONTRANDO VALOR ÓTIMO COM A BUSCA DA SEÇÃO ÁUREA
def buscaSecaoAurea(a, b, precisao):
	print("=" * 100)
	print("\nINÍCIO DA RESOLUÇÃO - BUSCA PELO MÉTODO DA SEÇÃO ÁUREA\n")
	print("=" * 100)
	print("\n")
	k = 1
	while True:
		p = a + 0.38197*(b - a)
		q = a + 0.61803*(b - a)
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
	precisao = float(input("Digite o valor da precisao: "))
	buscaSecaoAurea(a, b, precisao)
main()
