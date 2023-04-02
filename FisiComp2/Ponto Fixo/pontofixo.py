def pfix(a, b, e, f, phi):					# Recebe um intervalo [a,b], uma
											# precisão 'e', uma função f(x) e uma
											# função de interação phi(x).

	chi = (a+b) / 2  						# Aproximação inicial

	i = 1   								# Contador de iterações
	xn = chi
	while abs(f(xn)) > e:
		xn = phi(chi)
		print("Iteraçao: {:d} >> [{:.6f},{:.6f}] | chi = {:.6f} | f(chi) = {:.6f}".format(i, a, b, chi, f(chi)))
		i+=1
	print("Iteraçao: {:d} >> [{:.6f},{:.6f}] | chi = {:.6f} | f(chi) = {:.6f}".format(i, a, b, chi, f(chi)))

def f(x):
	return x**2 -5*x + 2 

def phi(x):
	return (x**2 + 2)/5

pfix(4.5, 4.6, 10**-3, f, phi)

