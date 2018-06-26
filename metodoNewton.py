from sympy import *
init_printing()
x, y = symbols('x y')
def f(x):
	return x**2 - 3*x + 2
def dfdx(xk,h):
	return (f(xk + h) - f(xk))/h
def dfdx2(xk,h):
    return dfdx(xk,h) - dfdx(xk,-h)/2*h
def newton(xa,xb,numeroIteracoes,erro,aproxInicial):
	xk = aproxInicial
	for i in range(numeroIteracoes):		
		if (xb-xa)/xb < erro:
			return xk
		xAnterior = xk
		xk = xAnterior - (diff(f(x),x).subs(x,xAnterior)/diff(diff(f(x),x),x).subs(x,xAnterior))
	return xk
def main():
	a = float(input("Digite o valor de xa: "))
	b = float(input("Digite o valor de xb: "))
	numeroIteracoes = int(input("Digite o numero de iteracoes: "))
	erro = float(input("Digite o erro: "))
	aproxInicial = float(input("Digite a aproximacao inicial: "))
	print('Raiz Aproximada:')
	print(newton(a,b,numeroIteracoes,erro,aproxInicial))
main()
