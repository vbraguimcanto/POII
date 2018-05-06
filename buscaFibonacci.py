#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CÁLCULO DA FUNÇÃO NO PONTO X
f = (lambda x: x**2 + 2*x)

# CÁLCULO DO NÚMERO DE ITERAÇÕES
w = (lambda a, b, e: (b-a)/e)

# LISTA DE FIBONACCI
def fibonacci(iteracoes):
	fib = []
	i = 0
	while True:
		if i == 0:
			fib.append(1)
		elif i == 1:
			fib.append(1)
		else:
			fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
		if(fib[len(fib) - 1]>iteracoes):
			return fib
		i+=1

def buscaFibonacci(a, b, fib, n):
	print("=" * 100)
	print("\nINÍCIO DA RESOLUÇÃO - BUSCA FIBONACCI\n")
	print("=" * 100)
	print("\n")
	k = 0
	while(k<n):
		p = a + (fib[n - k - 2])/(fib[n - k])*(b - a)
		q = a + ((fib[n - k - 1])/(fib[n - k]))*(b - a)
		print(k,'|', a,'|', b,'|', p,'|', f(p),'|', q,'|', f(q),'|')
		if f(p)>f(q):
			a = p
		else:
			b = q
		k+=1

def main():
	a = float(input("Digite o valor de A: "))
	b = float(input("Digite o valor de B: "))
	precisao = float(input("Digite o valor da precisao: "))
	iteracoes = w(a, b, precisao)
	fib = fibonacci(iteracoes)
	buscaFibonacci(a, b, fib, len(fib) - 1)
main()
