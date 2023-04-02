# UNIVERSIDADE FEDERAL DE MATO GROSSO DO SUL
# INSTITUTO DE FÍSICA
# FÍSICA COMPUTACIONAL E INFORMÁTICA
# Prof. Marcos Serrou do Amaral marcos.amaral@ufms.br

# ESTUDO DIRIGIDO: ZEROS REAIS DE FUNCÕES REAIS (ISOLAMENTO E MÉTODO DA BISSEÇÃO)

## 2) Considere a função f(x) = √x −5e^−x. Encontre uma raiz real dessa função no intervalo
## [1,4; 1,5] usando o Método da Bissecção. Inicialmente, utilize o método no papel fazendo
## todas as etapas até chegar em precisão igual ou inferior a 10-2.
## xk= a+b / 2

# Implementando o metodo da bisseccao (ED4 Fis. Comp. 1, adaptado):

def bissec(a, b, e, f): 					# Recebe um intervalo inicial [a,b],
											# um épsilon 'e' e uma função f(x).

	chi = (a+b)/2 							# chi: x aproximado, para cada iteração

	i = 1 									# Contador de interações
	print("Aprox.:", e)
	while f(chi) > e or f(chi) < -e:				# Iterage enquanto chi não cumpre
											# o requisito épsilon
		chi = (a+b)/2

		if f(a)*f(chi) > 0: 
			a = chi
		elif f(a)*f(chi) < 0: 
			b = chi
		 
		#print("Iteração:",i,">> [",a,",",b,"] 	| chi =", chi, "| f(chi) =",f(chi))
		print("Iteraçao: {:d} >> [{:.6f},{:.6f}] | chi = {:.6f} | f(chi) = {:.6f}".format(i, a, b, chi, f(chi)))
		if i > 100: 
			print(">> Limite de Iterações")
			return a, b, chi, f(chi)
		i+=1
	print(">> Aproximação da raiz: x = {:.12f}".format(chi))
	return chi, f(chi)  				# Retorna os valores de chi e f(chi)

# Escrevendo a funcao f(x) = √x −5e^−x :

import math as m

def f(x):
	return m.sqrt(x) - 5*m.e**(-x)

# Encontrando a raiz de f(x) pelo metodo da bisseccao
# epsilon = 10^-2
# Intervalo = [1,4; 1,5]
bissec(1.4, 1.5, 10**-2, f)

# epsilon = 10^-6
bissec(1.4, 1.5, 10**-8, f)


## 3) Altere os códigos apresentados para o isolamento e o método da bissecção para
## funcionarem num único código.

def isol(a, b, e, f):						# Busca intervalos de raizes de f(x) 
											# num intervalo [a, b] por isolamento, 
											# e refina a aproximacao por bisseccao
	i = 1
	for x in range(a, b):
		try: 
			if f(x-1) * f(x) < 0:
				print("Intervalo {:d} >> [{:.3f},{:.3f}]:".format(i,x-1,x))
				bissec(x-1, x, e, f)
				i += 1
		except ValueError: pass
		except ZeroDivisionError: pass
		x += 1

# Isolando as raizes de f(x) no intervalo [0, 50]
isol(0, 50, 10**-6, f)


## 4) No problema físico a seguir, equacione o problema e utilize o Método da Bissecção para
## encontrar a(s) raiz(es) e solucionar o problema. Em seguida, teste para outros valores de
## cargas e outras distâncias.
## Nos pontos A e B, separados pela distância AB = 3 m, fixam-se cargas elétricas puntiformes
## QA = 8 uC e QB = 2 uC, respectivamente. Determine um ponto onde o vetor campo elétrico é
## nulo. 

ko = 9*(10**9)				# Constante eletrostatica
							# no vacuo (N.m²/C²)

Q1 = 8*(10**-6)				# Valor das cargas
Q2 = 2*(10**-6)				# eletricas

# No ponto onde os campos de A e B se anulam, E(x) = 0
def E(x):
	y = (x**2)*(ko*Q2) - ((3-x)**2)*(ko*Q1)
	return y

chi, fchi = (bissec(-3, 3, 10**-4, E))

print("Ponto de campo eletrico nulo em x~={:.3f}m para Q1={:f}C e Q2={:f}C".format(chi, Q1, Q2))

# Outros valores


Q1 = 4*(10**-6) # Mesma proporcao, espera-se o mesmo valor que anteriormente
Q2 = 1*(10**-6)

chi, fchi = (bissec(-3, 3, 10**-4, E))

print("Ponto de campo eletrico nulo em x~={:.3f}m para Q1={:f}C e Q2={:f}C".format(chi, Q1, Q2))

Q1 = 5*(10**-4)
Q2 = 8*(10**-6)

chi, fchi = (bissec(-3, 3, 10**-3, E))

print("Ponto de campo eletrico nulo em x~={:.3f}m para Q1={:f}C e Q2={:f}C".format(chi, Q1, Q2))

