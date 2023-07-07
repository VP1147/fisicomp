### UNIVERSIDADE FEDERAL DE MATO GROSSO DO SUL
### INSTITUTO DE FÍSICA
### FÍSICA COMPUTACIONAL E INFORMÁTICA

### SISTEMAS LINEARES – MÉTODO DE GAUSS-JACOBI
### Prof. Marcos Serrou do Amaral marcos.amaral@ufms.br

import math as m
import matplotlib.pyplot as plt
import numpy as np

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

	#print(C)
	#print(x_0)
	#print(g)
	x_f = np.array( C.dot(x) + g )
	#print(x_f)
	return x_f


A = np.array([[10, 2, 1], [1, 5, 1], [2, 3, 10]])

B = np.array([7, -8, 6])

x_0 = np.array([0.7, -1.6, 0.6])
epsilon = 0.05

x = np.zeros(len(x_0))

# 2) Resolvendo o sistema linear

while abs(np.max(x) - np.max(x_0)) > epsilon:
	x_0 = x
	x = jacobi(A, B, x_0)
	print(x)
	print(abs(np.max(x) - np.max(x_0)))
	#print(x_0)

