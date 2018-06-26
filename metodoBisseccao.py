import sys, math
def f(x):
	return x**2 + math.log(x)
def bisseccao(erro,xa,xb):
	xk = (xa+xb)/float(2)
	while abs(xb - xa)/2 > erro:
		print f(xk)
		if f(xk) == 0:
			return xk
		elif f(xa)*f(xk) < 0:
			xb = xk
		else:
			xa = xk
		xk = (xa+xb)/float(2)
	return xk
def main():
	a = float(input("Digite o valor de xa: "))
	b = float(input("Digite o valor de xb: "))
	erro = float(input("Digite o valor do erro: "))
	print 'Raiz Aproximada:',
	print bisseccao(erro,a,b)
main()
