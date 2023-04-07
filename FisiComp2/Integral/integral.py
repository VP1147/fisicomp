import math as m

## (1) Comecando por integrais nao-numericas

# Integral(a_n*x^n)dx = (a_n*x^(n+1))/n+1

def indefint(n):	# Integral indefinida
	k=n
	j=n
	print("f(x) =", end=" ")
	while(k > 0):
		if k != n: print("+", end=" ")
		print("a_n*x^{:d}".format(k), end=" "); 
		k-=1
	print("\nF(x) =", end=" ")
	while(j > 0):
		if j != n: print("+", end=" ")
		print("a_n*x^{:d} /{:d}".format(j+1, j+1), end=" ")
		j -= 1
	print("+ c")
	print()

print("Para n = 2 :")
indefint(2) # a_n*x^2 + a_n-1*x

print("Para n = 4 :")
indefint(4)

def defint(n, a, b):	# Integral definida
	k=n
	j=n
	print("f(x) =", end=" ")
	while(k > 0):
		if k != n: print("+", end=" ")
		print("a_n*x^{:d}".format(k), end=" "); 
		k-=1
	print("\nIntervalo: [{:d},{:d}]".format(a, b))
	print("F(x) =", end=" ")
	while(j > 0):
		if j != n: print("+", end=" ")
		print("a_n*{:d}^{:d} /{:d}".format(b,j+1, j+1), end=" ")
		j -= 1
	j=n
	while(j > 0):
		print("-", end=" ")
		print("a_n*{:d}^{:d} /{:d}".format(a,j+1, j+1), end=" ")
		j -= 1
	print()

# Definindo os intervalos

a = 0
b = 1 

print("Para n = 2 :")
defint(2, a, b) # a_n*x^2 + a_n-1*x
print()

print("Para n = 4 :")
defint(4, a, b)


## (2) Integracao numerica

def f(x):			# f(x) = x^2
	return x**2

# Integracao numerica por soma de Riennmann (soma dos retangulos)
def integral(f, a, b):		# Integral de f(x) fx em [a,b]
	n = 10**6
	S = 0
	k=1
	i=a
	deltax = ((b-a)/n)
	while(k <= n):
		i += deltax
		S += f(i)*deltax
		k+=1
	print("n = {:d}".format(n))
	print("\nI: [{:d},{:d}]".format(a, b))
	print("S = {:.10f}".format(S))

integral(f, 0, 1)

def integral_t(f, a, b):	# Integral de f(x) dx em [a,b]
	print("\n>> Integral numerica de f(x)")
	n = 10**5
	S = 0
	k=1
	i=a
	deltax = (b-a)/n
	while(k <= n-1):
		i += deltax
		S += ((f(i) + f(i + deltax))/2)*deltax
		k+=1
	print("Iteracoes: 	{:d}".format(n))
	print("Intervalo: 	[{:.2f},{:.2f}]".format(a, b))
	print("Integral: 	{:.8f}".format(S))

integral_t(f, 0, 1)

# Explorando outras funcoes

def f(x):
	return m.sin(x)

integral_t(f, 0, m.pi)