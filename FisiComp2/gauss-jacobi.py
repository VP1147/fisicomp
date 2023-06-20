### UNIVERSIDADE FEDERAL DE MATO GROSSO DO SUL
### INSTITUTO DE FÍSICA
### FÍSICA COMPUTACIONAL E INFORMÁTICA

### SISTEMAS LINEARES – MÉTODO DE GAUSS-JACOBI
### Prof. Marcos Serrou do Amaral marcos.amaral@ufms.br

import math as m
import matplotlib.pyplot as plt

def jacobi(A, B, x_0):				# A - Matriz (a_nxn)
									# B - Matriz (b_n)
									# x0 - Aprox. inicial
	# Verifica o numero de linhas e colulas das matrizes dadas
	for An in range(0, len(A)): An+=1
	Bn = len(B)
	if An != Bn: return 0
	else: An = n
	# Imprime a forma das matrizes na tela
	print("A[{:d}x{:d}]".format(n, n))
	print("B[{:d}x1]".format(n))

	# Calcula C
	C = []
	for i in range(0, n):
		c = []
		for j in range(0, An):
			if i == j: c.append(0)
			else: c.append(-A[i][j]/A[i][i])
		C.append(c)
	# Calcula g
	g = []
	for i in range(0, An):
		

A = [10, 2, 1], [1, 5, 1], [2, 3, 10]

B = 7, -8, 6

x_0 = 0.7, -1.6, 0.6
epsilon = 0.05

jacobi(A, B, x_0)