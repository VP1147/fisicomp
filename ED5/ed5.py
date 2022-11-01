def f(x):
	return x**3 -9*x + 5

## Método da Posição Falsa

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
		 
		#print("Iteração:",i,">> [",a,",",b,"] 	| chi =", chi, "| f(chi) =",f(chi))
		print("Iteraçao: {:d} >> [{:.6f},{:.6f}] | chi = {:.6f} | f(chi) = {:.6f}".format(i, a, b, chi, f(chi)))
		chi = (a+b)/2
		if i > 100: 
			print(">> Limite de Iterações")
			return a, b, chi, f(chi)
		i+=1

	print(">> Aproximação da raiz: x = {:.6f}".format(chi))
	return a, b, chi, f(chi)  				# Retorna os valores de [a,b], chi e f(chi)

posfs(2, 3, 10**-2, f)