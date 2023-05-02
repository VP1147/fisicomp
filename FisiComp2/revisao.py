### REVISÃO PARA PROVA – INTEGRAÇÃO NUMÉRICA COM PROBLEMA FÍSICO

## Usando integração numérica, determine, graficamente, o potencial eletrostático,
## V(Z), em função da distância Z/R do centro de um disco uniformemente carregado
## σ : densidade superficial de carga e raio R.

import math as m
import numpy as np
import matplotlib.pyplot as plt

def simpson(f, a, b, n):	# Integral de f(x) dx no intervalo [a, b]
	i = 0  					# Contador de iteracoes
	d = 0
	h = (b-a)/n
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

R = 1				# m
Z = -3	 			# m
Sigma = 10e-9 		# C/m
e0 = 8.85e-12 		# C^2/N^2.m^2

def V(x):
	V = (2*m.pi*x)/m.sqrt((x**2)+((Z/R)**2))
	return V

A = Sigma / (4*m.pi*e0)

X = np.linspace(-3, 3, 1001)
Y = []
i = -3
while(i < 3):
	Y.append(A * simpson(V, 0, R, 100))
	Z += 6/(1000)
	i += 6/(1000)

fig, ax = plt.subplots()
plt.plot(X,Y, 'r')
ax.set_title('Potencial eletrostático V(Z) em função da distância Z/R do\n centro de um disco uniformemente carregado\n',
             fontsize = 10, fontweight ='bold')
plt.xlabel('Z/R', fontsize=9)
plt.ylabel('V', fontsize=9)
ax.grid()
plt.show()

