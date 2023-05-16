### UNIVERSIDADE FEDERAL DE MATO GROSSO DO SUL
### INSTITUTO DE FÍSICA
### FÍSICA COMPUTACIONAL E INFORMÁTICA
### EQUAÇÕES DIFERENCIAIS ORDINÁRIAS – MÉTODO DE EULER

### Prof. Marcos Serrou do Amaral - marcos.amaral@ufms.br
### Aluno: Vinicius A. Pavao - Eng. Fisica

import math as m
import matplotlib.pyplot as plt

def euler(f, h, yi, xf):
	xi = 0

	x = xi
	y = yi
	X = []
	Y = []
	while x <= xf :
		ya = f(x)
		dp = 100*(ya - y)/ya
		print("x = {:.2f} | y = {:.4f} | ya = {:.4f} | dp = {:.4f}%".format(x, y, ya, dp))
		Y.append(y)
		X.append(x)
		y += h*yh(x, y)
		x += h
	return X, Y

# Funcao da solucao analitica - para comparacao
def f(x):
	return (70/9)*m.e**(-0.3*x) - (43/9)*m.e**(-1.2*x)

# Eq. diferencial a ser resolvida - g(x,y)
def yh(x, y):
	return -1.2*y + 7*m.e**(-0.3*x)

# De 0 a 2.5
xf = 2.5

# y(0) = 3
yi = 3

# Eixos - passos de h = 0.5
euler(f, 0.5, yi, xf)


## Reproduzindo no grafico

# a = 0 e b = 7
xf = 7

# h = 0.1
h = 0.1

# Definindo os eixos de acordo com a resolucao
X, Y = euler(f, h, yi, xf)

fig = plt.figure()

# Linhas do eixo
plt.axhline(color='black', lw=0.5)
plt.axvline(color='black', lw=0.5)

# Desenhando o grafico
plt.plot(X, Y)
plt.show()
