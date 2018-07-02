import numpy as np
import math as mt
from sympy import *
init_printing()
x1, x2, v_lambda = symbols('x1 x2 v_lambda')
def f(x1, x2):
	return x1**2 - 2*x1*x2 + 4*(x2)**2

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

def gradiente(x0, g, erro):
    k = 1
    norma = 1000
    xk = x0
    g_tmp = g.subs(x1, xk[0])
    g_tmp = g_tmp.subs(x2, xk[1])
    norma_gradiente = calculaNorma(g_tmp)
    while norma > erro:
        d = (-1)*g_tmp
        x_novo = xk + v_lambda*d
        raiz = newton(0, 5, x_novo[0], x_novo[1], 20, erro)
        x_novo = x_novo.subs(v_lambda, raiz)
        xkAnterior = xk
        xk = x_novo
        g_tmp = g.subs(x1, xk[0])
        g_tmp = g_tmp.subs(x2, xk[1])
        norma_gradiente = calculaNorma(g_tmp)
        norma = calculaNorma(xk - xkAnterior)
    k+=1
    return xk
 
def main(): 
    x0 = Matrix([1, 1])
    erro = 0.1
    funcao = f(x1, x2)
    g = Matrix([diff(f(x1, x2), x1), diff(f(x1, x2), x2)])
    z = gradiente(x0, g, erro)
    print("Z* = ", z)
main()
