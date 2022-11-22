def f(x):									# f(x) = x³ -9x + 5
	return x**3 -9*x + 5

## Método da Posição Falsa
# Bastante similar ao método da bissecção, porém
# mais eficiente.

def posfs(a, b, e, f): 						# Recebe um intervalo inicial [a,b],
											# um épsilon 'e' e uma função f(x).

	chi = (a*f(b)-b*f(a))/(f(b)-f(a)) 		# chi: x aproximado, para cada iteração

	i = 1 									# Contador de interações

	while f(chi) > e or f(chi) < -e:		# Iterage enquanto chi não cumpre
											# o requisito épsilon
		if f(a)*f(chi) > 0: 
			a = chi
		elif f(a)*f(chi) < 0: 
			b = chi
		 
		# print("Iteraçao: {:d} >> [{:.6f},{:.6f}] | chi = {:.6f} | f(chi) = {:.6f}".format(i, a, b, chi, f(chi)))
		print("{:3d} {:.6f} {:.6f}".format(i, chi, f(chi)))
		chi = (a+b)/2
		if i > 100: 
			#print(">> Limite de Iterações")
			return a, b, chi, f(chi)
		i+=1
	print("{:3d} {:.6f} {:.6f}".format(i, chi, f(chi)))

posfs(0, 1, 10**-2, f)

## Método do Ponto Fixo
# As interações são feitas por uma função phi(x), onde f(x) = 0 <-> phi(x) = x

def phi(x): 								# Função de interação phi(x):
	return (x**3 + 5)/9 					# específica de f(x). Generalização
											# para qualquer f(x): a ser trabalhada

def pfix(a, b, e, f, phi):					# Recebe um intervalo [a,b], uma
											# precisão 'e', uma função f(x) e uma
											# função de interação phi(x).

	chi = (a+b) / 2  						# Aproximação inicial

	i = 0   								# Contador de iterações

	while abs(f(chi)) > e:
		# print("Iteraçao: {:d} >> chi = {:.6f} | f(chi) = {:.6f}".format(i, chi, f(chi)))
		print("{:3d} {:.6f} {:.6f}".format(i, chi, f(chi)))
		chi = phi(chi)
		i+=1
	print("{:3d} {:.6f} {:.6f}".format(i, chi, f(chi)))

pfix(0, 1, 10**-2, f, phi)


## Método de Newton: Melhoria do método do Ponto Fixo.
# É utilizada uma função de interação pré-determinada a partir da razão
# entre f(x) e sua derivada f'(x).

def df(x):								# Derivada de f(x) em x

	h = 0.00001
	return (f(x+h)-f(x))/h

def newton(a, b, e, f, df):				# Recebe um intervalo [a, b], uma
										# precisão 'e', uma função f(x) e sua
										# derivada df(x).

	chi = (a+b) / 2  					# Aproximação inicial

	i = 0   							# Contador de iterações
	
	while abs(f(chi)) > e:
		print("{:3d} {:.6f} {:.6f}".format(i, chi, f(chi)))
		chi = chi - (f(chi) / df(chi))
		i += 1
	print("{:3d} {:.6f} {:.6f}".format(i, chi, f(chi)))

newton(0, 1, 10**-2, f, df)
