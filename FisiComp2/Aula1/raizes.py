# Encontrando Raizes: isolamento e refinamento

import math as m

# f(x) = x^2 = 4 = 0
def f(x):
	y = x**2 - 4
	return y

# Buscando a raiz no intervalo -100 a 100 e precisao 1
for x in range(-100, 100):
	#print(x, f(x))
	x += 1

# f(x) = x^3 - 9x + 3
def g(x):
	y = x**3 -9*x + 3
	return y

for x in range(-10, 10):
	if g(x-1) * g(x) < 0:
		# print(x-1, g(x-1))
		# print(x, g(x))
		print("Raiz entre ",x-1," e",x)
	x += 1

# Verificacao por derivada numerica

## Funcao que determina derivada numerica de f em x
def df(f, x):
	dx = 0.001
	dy = (f(x + dx) - f(x)) / dx
	return dy

for x in range(-10, 10):
	if g(x-1) * g(x) < 0:
		# print(x-1, g(x-1))
		# print(x, g(x))
		print("Raiz entre ",x-1," e",x)
	x += 1

## Fazendo a derivada numerica nos intervalos encontrados
dx = 0.2
flag = 0

def root(f): 
	for x in range(-100, 100):
		if g(x-1) * g(x) < 0:
			xl = x - 1
			print(">> ({:d},{:d})".format(x-1, x))
			while(xl < x):
				if df(g, xl) * df(g, xl + dx) < 0: flag += 1
				if flag == 0: print("Apenas uma raiz em",xl,",", xl+dx)
				xl += dx
		x += 1

def f(x):
	return m.sqrt(x) - 5*m.e**(-x)

def bissec(a, b, e, f): 					# Recebe um intervalo inicial [a,b],
											# um épsilon 'e' e uma função f(x).

	chi = (a+b)/2 							# chi: x aproximado, para cada iteração

	i = 1 									# Contador de interações

	while f(chi) > e or f(chi) < -e:		# Iterage enquanto chi não cumpre
											# o requisito épsilon
		if f(a)*f(chi) > 0: 
			a = chi
		elif f(a)*f(chi) < 0: 
			b = chi
		 
		#print("Iteração:",i,">> [",a,",",b,"] 	| chi =", chi, "| f(chi) =",f(chi))
		print("Iteraçao: {:d} >> [{:.6f},{:.6f}] | chi = {:.6f} | f(chi) = {:.6f}".format(i, a, b, chi, f(chi)))
		chi = (a+b)/2
		if i > 100: 
			print(">> Limite de Iterações")
			return a, b, chi, f(chi)
		i+=1

	print(">> Aproximação da raiz: x = {:.6f}".format(chi))
	return a, b, chi, f(chi)  				# Retorna os valores de [a,b], chi e f(chi)

a = 1.4
b = 1.5
bissec(a, b, 0.00001, f)

def f(x):
	return x**3 -9*x +3
