### UNIVERSIDADE FEDERAL DE MATO GROSSO DO SUL - INSTITUTO DE FÍSICA
### FÍSICA COMPUTACIONAL E INFORMÁTICA
### Prof. Marcos Serrou do Amaral marcos.amaral@ufms.br
### AVALIAÇÃO P01 – 2023.01 - 04 / MAIO / 2023
### ALUNO: Vinicius Arruda Pavao

## 1) (5,0 pontos) 

# Implementacao da Regra de 1/3 de Simpson

import math as m
import numpy as np
import matplotlib.pyplot as plt

def simpson(f, a, b, n, y):	# Integral de f(x) dx no intervalo [a, b]
	i = 0  					# Contador de iteracoes
	d = 0
	h = (b-a)/n
	S = 0
	while(i <= n):
		if i == 0 or i == n: 	S += f(d, y)
		elif i % 2 != 0: 		S += 4*f(d, y)
		elif i % 2 == 0: 		S += 2*f(d, y)
		d += h
		i += 1
	S = S*(h/3)
	#print("> {:.8f}".format(S))
	return S

# Definindo os valores para a equacao

l = 2					# Comprimento (m)
y = [-15, 15] 			# Intervalo y (m)
Lambda = 1*10**-6 		# C/m
e0 = 8.85e-12 			# C^2/N^2.m^2

# Funcao a ser integrada em x (y varia no grafico)
def V(x, y):
	try: 	V = 1/m.sqrt((x**2)+(y**2))
	except: V = 0 							# No caso de divisao por zero
	return V

# Valor que multiplica a integral
A = Lambda / (4*m.pi*e0)

# Define os espacos lineares para o grafico (x, y)
X = np.linspace(-1, 1, 31)
Y = []

# Define o valor de Y para cada X (-15, 15)
i = y[0]
while(i <= y[1]):
	Y.append(A * simpson(V, -l/2, l/2, 10, i))
	i += 1

# Desenha o grafico
fig = plt.figure()
plt.plot(X,Y, 'r')
plt.show()

## 2) (5,0 pontos) 

# Implementando a regra de 3/8 de Simpson
def simpson38(f, a, b, n):		# Integral de f(x) dx no intervalo [a, b]
	i = 0  						# Contador de iteracoes
	k = a
	h = (b-a)/(3*n)				# Dividindo os subintervalos
	S = 0						# Variavel de soma
	while(i <= (3*n)-3):
		try: S += f(k) + 3*f(k + h) + 3*f(k + 2*h) + f(k + 3*h)
		except: pass
		i += 3
		k += 3*h
	S = S*((3*h)/8)

	#print("I ~= {:.12f}".format(S))
	return S

# Funcao a integrar
def f(x):
	return m.exp(x)

# Intervalo
a, b = 0, 3

# Calculando a integral de f(x) pela regra de 3/8 de Simpson
# no intervalo [a, b] e 6 subdivisoes
Sp = simpson38(f, a, b, 2)					# 6 = 3*n, n = 2

# Resultado analitico
Al = m.exp(3) - m.exp(0)

# Comparando os resultados e apresentando o erro percentual
print("Int. Simpson ~= {:.12f}".format(Sp))
print("Int. Analitico = {:.12f}".format(Al))
print("Erro = {:.12f}%".format(((Sp-Al)/Sp)*100))