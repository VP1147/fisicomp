# Zeros de funcoes reais
# Metodo de Newton

def isol(a, b, f):

	for x in range(a, b):
		if f(x-1) * f(x) < 0:
			print("[{:d},{:d}]".format(x-1,x))
		x += 1

def newton(a, b, e, f, df):				# Recebe um intervalo [a, b], uma
										# precisão 'e' e uma função f(x) 

	chi = (a+b) / 2  					# Aproximação inicial

	i = 1   							# Contador de iterações
	
	while abs(f(chi)) > e:
		print("Iteraçao: {:d} >> [{:.6f},{:.6f}] | chi = {:.6f} | f(chi) = {:.6f}".format(i, a, b, chi, f(chi)))
		chi = chi - (f(chi) / df(chi))
		i += 1
	print("Iteraçao: {:d} >> [{:.6f},{:.6f}] | chi = {:.6f} | f(chi) = {:.6f} <<".format(i, a, b, chi, f(chi)))


def f(x):				# f(x) = x2 -5x +2
	return x**2 -5*x + 2

def df(x):				# Derivada de f(x) em x

	h = 10**-3
	return (f(x+h)-f(x))/h

isol(-1000, 1000, f)
newton(0, 1, 10**-6, f, df)
newton(4, 5, 10**-6, f, df)
