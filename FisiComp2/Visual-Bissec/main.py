from tg import tg
import math as m
from getch import getch

def f(x):				# f(x) = x2 -5x +2
	return x**2 -5*x + 2

markers = [0]

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
		markers.append(round(chi,2))
		if i > 100: 
			print(">> Limite de Iterações")
			return a, b, chi, f(chi)
		i+=1

	print(">> Aproximação da raiz: x = {:.6f}".format(chi))
	return a, b, chi, f(chi)  				# Retorna os valores de [a,b], chi e f(chi)

tg.theme("./tg/dark.json")
tg.init(800, 10, 1)

a = -6
b = 6
bissec(a, b, 10**-3, f)

set_res = set(markers)
tg.Mkrs = list(set_res)
tg.Mkrs.sort()
print(markers)
print(tg.Mkrs)

tg.plot(f)

getch()