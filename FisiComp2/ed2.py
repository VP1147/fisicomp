# UNIVERSIDADE FEDERAL DE MATO GROSSO DO SUL
# INSTITUTO DE FÍSICA
# FÍSICA COMPUTACIONAL E INFORMÁTICA
# Prof. Marcos Serrou do Amaral marcos.amaral@ufms.br

# ESTUDO DIRIGIDO: INTEGRAÇÃO NUMÉRICA – REGRA DOS TRAPÉZIOS e 
# REGRA 1/3 de SIMPSON

# 2) Implementacao em Python de metodos de integracao
# numerica: Regra dos trapezios e Regra de 1/3 de Simpson

def trapz(f, a, b, m):	# Integral de f(x) dx no intervalo [a, b]
	i = 0  				# Contador de iteracoes
	d = 0
	h = (b-a)/m
	S = 0
	print("\n>> Regra dos Trapezios")
	print(">> h = {:.2f}, m = {:.2f}".format(h, m))
	while(i <= (m-1)):
		S += (f(d)+f(d+h))
		#print("{:d} : {:.2f} + {:.2f}".format(i, f(d),f(d+h)))
		i += 1
		d += h
	S = (h/2)*S
	print("> {:.8f}".format(S))
	return S

def f(x):
	fx = [1,1,0,-1,2]
	return fx[int(x)]


trapz(f, -1, 3, 4)

def simpson(f, a, b, n):	# Integral de f(x) dx no intervalo [a, b]
	i = 0  					# Contador de iteracoes
	h = (b-a)/n
	d = a
	S = 0
	#print("\n>> Regra de 1/3 Simpson")
	#print(">> h = {:.2f}, n = {:.2f}".format(h, n))
	while(i <= n):
		if i == 0 or i == n: 
			S += f(d)
			#print("{:d} : S + {:.2f}".format(i, f(d)))
		elif i % 2 != 0: 
			S += 4*f(d)
			#print("{:d} : S + 4*{:.2f}".format(i, f(d)))
		elif i % 2 == 0: 
			S += 2*f(d)
			#print("{:d} : S + 2*{:.2f}".format(i, f(d)))
		d += h
		i += 1
	S = S*(h/3)
	print("> {:.8f}".format(S))
	return S

simpson(f, -1, 3, 4)

# a) Utilizando seu código em Python do item anterior, calcule uma aproximação para
# I usando 10 subintervalos e as regras dos Trapézios e de 1/3 de Simpson.

import math as m
def I(x):		# Funcao integranda de I
	return m.e**x

St = trapz(I, 0, 1, 10)
print("Erro = {:.12f}%".format(((St-(m.e-1))/St)*100))
Ss = simpson(I, 0, 1, 10)
print("Erro = {:.12f}%".format(((Ss-(m.e-1))/Ss)*100))

# Erro relativo para 100 iteracoes

St = trapz(I, 0, 1, 100)
print("Erro = {:.12f}%".format(((St-(m.e-1))/St)*100))
Ss = simpson(I, 0, 1, 100)
print("Erro = {:.12f}%".format(((Ss-(m.e-1))/Ss)*100))

# Erro relativo para 1000 iteracoes

St = trapz(I, 0, 1, 1000)
print("Erro = {:.12f}%".format(((St-(m.e-1))/St)*100))
Ss = simpson(I, 0, 1, 1000)
print("Erro = {:.12f}%".format(((Ss-(m.e-1))/Ss)*100))

def dN(x):
	return m.e**(-x)

St = trapz(dN, 0, 1, 1000)
Ss = simpson(dN, 0, 1, 1000)

# Matplotlib

import matplotlib.pyplot as plt
import numpy as np

#x = np.linspace(-5,5,100)
#y = -m.e**(-x)

#fig = plt.figure()
#plt.plot(x,y, 'r')

#plt.show()

## 5)

l = 1				# m
y = -10 			# m
Lambda = 10e-10 		# C/m
e0 = 8.85e-12 		# C^2/N^2.m^2

def V(x):
	V = 1/m.sqrt((x**2)+(y**2))
	return V

A = Lambda / (4*m.pi*e0)

print("Lambda = {:6f}	l = {:.2f}	y = {:.2f}".format(Lambda, l, y))
print("V = {:.2f}".format(A*Ss))

X = np.linspace(-10, 10, 1000)
Y = []
i = -10
while(i < 10):
	Y.append(A * simpson(V, -l/2, l/2, 100))
	y += 20/(1000-1)
	i += 20/(1000-1)

fig = plt.figure()

plt.plot(X,Y, 'r')

plt.show()

