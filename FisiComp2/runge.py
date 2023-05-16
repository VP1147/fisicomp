### UNIVERSIDADE FEDERAL DE MATO GROSSO DO SUL
### INSTITUTO DE FÍSICA
### FÍSICA COMPUTACIONAL E INFORMÁTICA

### EQUAÇÕES DIFERENCIAIS ORDINÁRIAS – MÉTODO DE RUNGE-KUTTA
### Prof. Marcos Serrou do Amaral marcos.amaral@ufms.br

import math as m

def runge(f, fa, h, y0, xf):		# f(x, y) = dy/dx | h - tamanho das subdivisoes
									# 
	xi = 0
	x = xi							# Valores iniciais
	y = yi
	X = []							# Listas
	Y = []

	while x <= xf:
		k1 = h * f(x, y)				# Primeiro ponto - Metodo de Euler
		y1 = y + k1

		k2 = h * f(x + h, y1)
		y += 0.5 * (k1 + k2)

		ya = fa(x+h)
		dp = 100*abs(ya - y)/ya
		print("x = {:.2f} | y = {:.4f} | ya = {:.4f} | dp = {:.4f}%".format(x, y, ya, dp))

		Y.append(y)
		X.append(x)

		x += h
	return X, Y

# Funcao da solucao analitica - para comparacao
def fa(x):
	return (70/9)*m.e**(-0.3*x) - (43/9)*m.e**(-1.2*x)

# Eq. diferencial a ser resolvida - g(x,y)
def f(x, y):
	return -1.2*y + 7*m.e**(-0.3*x)


xf = 7
yi = 3
h = 0.1

runge(f, fa, h, yi, xf)