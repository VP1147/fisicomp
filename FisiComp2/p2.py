### UNIVERSIDADE FEDERAL DE MATO GROSSO DO SUL - INSTITUTO DE FÍSICA
### FÍSICA COMPUTACIONAL E INFORMÁTICA
### Prof. Marcos Serrou do Amaral marcos.amaral@ufms.br
### AVALIAÇÃO P02 – 2023.01 - 29 / JUNHO / 2023
### ALUNO: Vinicius Arruda Pavao

## 1) (5,0 pontos) Método de Runge-Kutta

# Define as bibliotecas utilizadas
import math as m
import matplotlib.pyplot as plt

# Resolve equações diferenciais ordinárias pelo método de Runge-Kutta
# de 2a ordem.
def runge2(f, h, y0, xi, xf):	# f(x, y) = dy/dx | h - tamanho das subdivisoes
									# 
	x = xi							# Valores iniciais
	y = yi
	X = []							# Listas
	Y = []
	# Calcula enquanto x é menor ou igual a xf (argumento)
	while x <= xf:
		k1 = h * f(x, y)				# Primeiro ponto - Metodo de Euler
		y1 = y + k1

		k2 = h * f(x + h, y1)
		y += 0.5 * (k1 + k2)
		Y.append(y)
		X.append(x)
		x += h
	return X, Y

# Eq. diferencial a ser resolvida - g(x,y)
def f(x, y):
	return -1.3*y + 5*m.e**(-0.2*x)

# Valores iniciais e finais de x
xi = 0
xf = 8
# Valor inicialÇ y(0)
yi = 2
# Passo: Intervalo entre as subdivisões
h = 0.01

# Definindo os eixos de acordo com os retornos da função
X, Y = runge2(f, h, yi, xi, xf)
# Define a figura na biblioteca matplotlib.pyplot
fig = plt.figure()
# Desenha as linhas do eixo
plt.axhline(color='black', lw=0.5)
plt.axvline(color='black', lw=0.5)
# Desenha e mostra o gráfico
plt.plot(X, Y)
plt.show()

## 2) (5,0 pontos) Método de Gauss-Jacobi

# Define a biblioteca utilizada
import numpy as np

# Resolve sistemas lineares a partir do método de Gauss-Jacobi
def jacobi(A, B, x_0):				# A - Matriz (a_nxn)
									# B - Matriz (b_n)
									# x0 - Aprox. inicial

	# Verifica o numero de linhas e colulas das matrizes dadas
	A = np.array(A)
	B = np.array(B)
	x = np.array(x_0)
	if len(A) == len(B) == len(x):
		n = len(A)
	else: return 0

	# Calcula C
	C = np.zeros((n, n))
	for i in range(0, n):
		for j in range(0, n):
			if i == j: C[i][j] = 0
			else: C[i][j] = (-A[i][j]/A[i][i])
	# Calcula g
	g = np.zeros(n)
	for i in range(0, n):
		g[i] = (B[i]/A[i][i])

	x_f = np.array( C.dot(x) + g )

	return x_f


A = np.array([[10, 2, 1], [1, 5, 1], [2, 3, 10]])

B = np.array([7, -8, 6])

x_0 = np.array([0.7, -1.6, 0.6])
epsilon = 0.05

x = np.zeros(len(x_0))

# Iterações para resolver o sistema linear: itera até atingir um
# erro menor que epsilon
i=1
while abs(np.max(x) - np.max(x_0)) > epsilon:
	x_0 = x
	x = jacobi(A, B, x_0)
	print("[{:d}] --> ".format(i))
	print(x)
	print("e = {:.6f}".format(abs(np.max(x) - np.max(x_0))))
	#print(x_0)
	i += 1