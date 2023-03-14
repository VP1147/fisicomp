# Encontrando Raizes: isolamento e refinamento

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
for x in range(-10, 10):
	if g(x-1) * g(x) < 0:
		xl = x - 1
		while(xl < x):
			print(xl, df(g, xl))
			xl += dx
	x += 1

