import numpy as np
import math as mt
from sympy import *
init_printing()
x1, x2, v_lambda = symbols('x1 x2 v_lambda')
def f(x1, x2):
	return (x1 - 2)**4 + (x1 - 2*x2)**2

def calculaNorma(xkAtual, xkAnterior):
    sub = xkAtual - xkAnterior
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

def coordenadasCiclicas(x0, erro):
    k = 1
    xk  = x0
    yj = xk
    # Norma com valor alto para iniciar as iterações
    #print(erro)
    norma = 1000
    while norma > erro:
        # F(Xk) recebe o primeiro e o segundo elemento da matriz, sendo respectivamente x1 e x2
        fxk = f(xk[0],xk[1])
        # J recebe 1 em uma iteração e 2 na outra
        for j in range(0,2):
            # J na primeira iteração, recebe d = (0, 1)
            if j == 0:
                d = Matrix([1, 0])
                yj1 = xk + v_lambda*d
                raiz = round(newton(0, 5, yj1[0], yj1[1], 20, erro), ndigits=2)
                yj1 = yj1.subs(v_lambda, raiz)
                y = yj1
            # J na primeira iteração, recebe d = (1, 0)
            elif j == 1:
                d = Matrix([0, 1])
                yj1 = y + v_lambda*d
                raiz = round(newton(0, 5, yj1[0], yj1[1], 20, erro), ndigits=2)
                yj1 = yj1.subs(v_lambda, raiz)
                xkAnterior = xk
                xk = yj1
                norma = calculaNorma(xk, xkAnterior)

    return xk

def main(): 
    x0 = Matrix([0, 3])
    erro = 0.1
    z = coordenadasCiclicas(x0, erro)
    print("Z* = ", z)
main()
