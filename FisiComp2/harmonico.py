### UNIVERSIDADE FEDERAL DE MATO GROSSO DO SUL
### INSTITUTO DE FÍSICA
### FÍSICA COMPUTACIONAL E INFORMÁTICA
### EQUAÇÕES DIFERENCIAIS ORDINÁRIAS – MÉTODO DE RUNGE-KUTTA
### Prof. Marcos Serrou do Amaral marcos.amaral@ufms.br

import math as m
import matplotlib.pyplot as plt

## Implementando o METODO DE RUNGE-KUTTA (4a Ordem)
# O metodo na 4a ordem produz uma precisao muito superior
# ao metodo na 2a ordem.

# Metodo de Runge-Kutta de 4a ordem
# Delimitado por xf, iterage (xf - x) / h vezes
def runge4h(f, fa, h, y0, xf):		# f(x, y) = dy/dx | h - tamanho das subdivisoes
									# 
	xi = 0
	x = xi							# Valores iniciais
	y = yi
	X = []							# Listas
	Y = []

	while x <= xf:

		k1 = h * f(x, y)				# Primeiro ponto - Metodo de Euler
		k2 = h * f(x + h/2, y + k1/2)
		k3 = h * f(x + h/2, y + k2/2)
		k4 = h * f(x + h, y + k3)

		y += (1/6) * (k1 + 2*k2 + 2*k3 + k4)
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

# Variaveis iniciais
xf = 7
yi = 3

# h = 0.1
h = 0.1

# Definindo os eixos de acordo com a resolucao
# Chamando a funcao na 4a ordem
X, Y = runge4h(f, fa, h, yi, xf)

#fig = plt.figure()

# Linhas do eixo
#plt.axhline(color='black', lw=0.5)
#plt.axvline(color='black', lw=0.5)

# Desenhando o grafico
#plt.plot(X, Y)
#plt.show()

## 2) Para resolver uma Equação Diferencial Ordinária (EDO) de segunda ordem usando
## o método de Runge-Kutta, é necessário reformular a equação como um sistema de
## duas EDOs de primeira ordem. Essa reformulação envolve a introdução de uma
## nova variável para representar a derivada da variável desconhecida de segunda
## ordem.

# Metodo de Runge-Kutta de 4a ordem, adaptado para equacoes diferenciais
# ordinarias de 2a ordem.
# Delimitado por xf, iterage n vezes

def dv(x, omega):
	return -omega*omega*x

def harmonico(t0, x0, v0, h, n):		# f(x, y), g(x, y) | h - tamanho das subdivisoes

	# Valores iniciais
	t = t0
	v = v0
	x = x0
	X = []
	V = []
	T = []

	omega = 1
	i = 1							# Contador de iteracoes

	while i <= n:

		k1v = h * dv(x, omega)
		k1x = h * v

		k2v = h * dv(x + k1v/2, omega)
		k2x = h * (v + k1x/2)

		k3v = h * dv(x + k2v/2, omega)
		k3x = h * (v + k2x/2)

		k4v = h * dv(x + k3v, omega)
		k4x = h * (v + k3x)

		v += (1/6) * (k1v + 2*k2v + 2*k3v + k4v)
		x += (1/6) * (k1x + 2*k2x + 2*k3x + k4x)
		#ya = fa(x+h)
		#dp = 100*abs(ya - y)/ya
		print("{:d} -> t = {:.2f} | v = {:.2f} | x = {:.4f}".format(i, t, v, x))

		V.append(v)
		X.append(x)
		T.append(t)
		
		t += h
		i += 1

	return X, V, T


t0 = 0
x0 = 1
v0 = 0
h = 0.01
n = 1000

X, V, T = harmonico(t0, x0, v0, h, n)

fig = plt.figure()

plt.plot(T, X)
plt.plot(T, V)

plt.grid()
plt.show()