import numpy as np
import math as mt
from sympy import *
init_printing()
x1, x2, v_lambda = symbols('x1 x2 v_lambda')
def f(x1, x2):
	return (x1 - 2)**4 + (x1 - 2*x2)**2

def newton(xa, xb, y1, y2, numeroIteracoes, erro):
	xk = xa
	funcao = f(y1, y2)
	primeiraDerivada = diff(funcao, v_lambda)
	segundaDerivada = diff(primeiraDerivada, v_lambda)
	print(primeiraDerivada)
	print(segundaDerivada)
	for i in range(numeroIteracoes):
		if (xb-xa)/xb < erro:
			return xk
		xAnterior = xk
		primeiraDerivadaValor = float(primeiraDerivada.subs(v_lambda,xAnterior))
		segundaDerivadaValor = float(segundaDerivada.subs(v_lambda, xAnterior))
		xk = xAnterior - (primeiraDerivadaValor/segundaDerivadaValor)	
	return xk

def coordenadasCiclicas(x0, erro):
    k = 0
    xk  = x0
    # Norma com valor alto para iniciar as iterações
    norma = 1000
    while norma > erro:
        # F(Xk) recebe o primeiro e o segundo elemento da matriz, sendo respectivamente x1 e x2
        fxk = f(xk[0],xk[1])
        # J recebe 1 em uma iteração e 2 na outra
        for j in range(1,3):
            # J na primeira iteração, recebe d = (0, 1)
            if j == 1:
                d = Matrix([1, 0])
            # J na primeira iteração, recebe d = (1, 0)
            else:
                d = Matrix([0, 1])
                break
            # Caso for a primeira iteração, ou seja, a norma foi definida como muito alta para que o primeiro Y, receba Xk (Yj+1 = Xk + λdj)
            if(norma == 1000):
                yj = xk + v_lambda*d
                raiz = newton(xk[0], xk[1], yj[0], yj[1], 20, erro)
                yj = yj.subs(v_lambda, raiz)
                print(round(raiz, 2))
                print(yj)
            # Caso não for a primeira iteração, Yj+1 = Yj + λdj
            else:
                yj1 = yj + v_lambda*d
                raiz = newton(xk[0], xk[1], yj1[0], yj1[1], 20, erro)
                yj1 = yj + raiz*d
        break

def main(): 
    x0 = Matrix([0, 3])
    erro = 0.1
    x = coordenadasCiclicas(x0, erro)

    #print(m)
    #print(diff(f(x1),x1))




main()
