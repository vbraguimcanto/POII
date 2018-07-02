#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import math as mt
from sympy import *
init_printing()
x1, x2, v_lambda = symbols('x1 x2 v_lambda')
def f(x1, x2):
	return (x1 - 2)**4 + (x1 - 2*x2)**2

def calculaNorma(vetor):
    sub = vetor
    for p in range(0,2):
        if (p == 0):
            soma = round(mt.pow(sub[p], 2), ndigits=2)            
        else:
            soma = round(soma + mt.pow(sub[p], 2), ndigits=2)
    return mt.sqrt(soma)

def newton(xa, xb, y1, y2, numeroIteracoes, erro):
    xk = xa
    funcao = f(y1, y2)
    primeiraDerivada = diff(funcao, v_lambda)
    segundaDerivada = diff(primeiraDerivada, v_lambda)
    for i in range(numeroIteracoes):
        if abs(xb - xa) >= 1:
            if abs((xb-xa)/xb) < erro:
                return xk
        else:
            if abs(xb-xa) < erro:
                return xk
        xAnterior = xk
        primeiraDerivadaValor = float(primeiraDerivada.subs(v_lambda,xAnterior))
        segundaDerivadaValor = float(segundaDerivada.subs(v_lambda, xAnterior))
        xk = xAnterior - (primeiraDerivadaValor/segundaDerivadaValor)
    return xk

def metodoNewton(x0, g, matrizHessiana, erro):
    k = 1
    norma = 1000
    xk = x0
    g_tmp = g.subs(x1, xk[0])
    g_tmp = g_tmp.subs(x2, xk[1])

    matrizHessiana_tmp = matrizHessiana.subs(x1, xk[0])
    matrizHessiana_tmp = matrizHessiana_tmp.subs(x2, xk[1])
    matrizHessiana_tmpInversa = matrizHessiana_tmp.inv("LU")
    norma_gradiente = calculaNorma(g_tmp)

    while norma > erro:
        # Cálculo do novo d
        d = (-1)*matrizHessiana_tmpInversa*(g_tmp)

        # Cálculo do novo X
        x_novo = xk + v_lambda*d

        # Cálculo da Raiz
        raiz = newton(0, 5, x_novo[0], x_novo[1], 20, erro)

        # Substituição do valor de lambda pela raiz
        x_novo = x_novo.subs(v_lambda, raiz)

        # Armazenando o Xk anterior para comparação
        xkAnterior = xk
        xk = x_novo

        # Cálculo do novo gradiente (via no ponto X)
        g_tmp = g.subs(x1, xk[0])
        g_tmp = g_tmp.subs(x2, xk[1])

        # Cálculo da matriz Hessiana nos novos pontos
        matrizHessiana_tmp = matrizHessiana.subs(x1, xk[0])
        matrizHessiana_tmp = matrizHessiana_tmp.subs(x2, xk[1])

        # Cálculo da matriz hessiana invversa
        matrizHessiana_tmpInversa = matrizHessiana_tmp.inv("LU")

        # Cálculo da norma do gradiente
        norma_gradiente = calculaNorma(g_tmp)

        # Cálculo da norma do vetor Xk - Xkanterior
        norma = calculaNorma(xk - xkAnterior)
    k+=1
    return xk

def main(): 
    x0 = Matrix([0, 3])
    erro = 0.1
    funcao = f(x1, x2)
    g = Matrix([diff(f(x1, x2), x1), diff(f(x1, x2), x2)])

    # Primeira linha e coluna da matriz hessiana
    x11 = diff(funcao, x1)
    x11 = diff(x11, x1)

    # Primeira linha e segunda coluna da matriz hessiana
    x12 = diff(funcao, x2)
    x12 = diff(x12, x1)

    # Segunda linha e primeira coluna da matriz hessiana
    x21 = diff(funcao, x1)
    x21 = diff(x21, x2)
    
    # Segunda linha e segunda coluna da matriz hessiana
    x22 = diff(funcao, x2)
    x22 = diff(x22, x2)

    matrizHessiana = Matrix([[x11, x12],[x21, x22]])
    z = metodoNewton(x0, g, matrizHessiana, erro)
    print("Z* = ", z)
main()
