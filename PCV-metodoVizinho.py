#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from numpy import genfromtxt

def calculaValorOtimo(df, listaMenores):
	z = 0
	for l in range(0, len(listaMenores)):
		x, y = listaMenores[l].split(',')
		x = x.replace("(", "")
		y = y.replace(")", "")
		z += df[int(x), int(y)]
	return z

def tratDiagonalPrincipal(df, n):
	for i in xrange(0,n):
		for j in xrange(0,n):
			if i == j:
				df[i][j] = 1000000
	return df

def buscaMenoresMatriz(df, n):
	listaMenores = []
	for p in range(0,n):
		for i in range(0,n):
			for j in range(0,n):
				if i == 0 and j == 0:
					menorElemento = df[i,j]
					menorElementoX = i
					menorElementoY = j
				else:
					if df[i][j] < menorElemento and ("("+ str(i) + "," + str(j) +")") not in listaMenores:
						menorElemento = df[i,j]
						menorElementoX = i
						menorElementoY = j
		if ("("+ str(i) + "," + str(j) +")") not in listaMenores:
			listaMenores.append("("+ str(menorElementoX) + "," + str(menorElementoY) + ")")			
			df[menorElementoY, menorElementoX] = 1000000
			for r in range(0,n):
				if r != menorElementoY:
					df[menorElementoX,r] = 1000000
			for r in range(0,n):
				if r != menorElementoX:
					df[r,menorElementoY] = 1000000
	return listaMenores, df

def main():
	df = genfromtxt('base-custo-CSV.csv', delimiter=';')
	n = len(df)
	df = tratDiagonalPrincipal(df, n)
	listaMenores, df_mod = buscaMenoresMatriz(df, n)
	z = calculaValorOtimo(df, listaMenores)
	print 'Z* = ', z
main()
