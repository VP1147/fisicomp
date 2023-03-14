# ESTUDO DIRIGIDO 04: ZEROS REAIS DE FUNCÕES REAIS (ISOLAMENTO E MÉTODO DA BISSEÇÃO)
# Vídeo-aulas para referência e estudos:
# CNUM-003 Zeros de Funções – Isolamento de Raízes: https://youtu.be/eUqWM2VROJw
# CNUM-004 Zeros de Funções – Método da Bissecção: https://youtu.be/AA3QNwHM41o

## 1) [Resolvida em papel]

## 2) Considere a função f(x) = x³ – 9x + 5 no intervalo [0,3]. 
## Implemente um código que indique quais sub-intervalos de [0,3] 
## temos as raízes de f(x).

# Define-se o intervalo [0,3]
i = [-10,10]

# Declara-se a função f(x):
def f(x):
	return x**3 -9*x + 5


p = 1 				# Período de busca: 0.1
k = i[0]			# Início
while k <= i[1]:	# Busca sub-intervalos com raízes dentro do intervalo i
	if f(k-p)*f(k) < 0: 
		print(" >> Há ao menos uma raiz no intervalo ["
			+str(round(k-p,3))+", "+str(round(k,3))+"]")
	k += p

## 3) [Resolvida em papel]

## 4) Implemente o Método da Bisseção para refinar os sub-intervalos obtidos no item
## (2) e obter os resultados para o item (3). Obtenha as raízes da função
## f(x) = x³ – 9x+ 5 utilizando ε = 10^-2 como critério de parada ou k > 100.

# Bibliotecas necessárias
import math as m

# Implementando o método da bissecção

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

# Para a função f(x) = x³ -9x + 5, com épsilon = 10^-2, no intervalo [0.5, 1]
bissec(0.5, 1, 10**-2, f)

# Para a função f(x) = x³ -9x + 5, com épsilon = 10^-2, no intervalo [-4, -3]

bissec(-4, -3, 10**-2, f)

# Para a função f(x) = x³ -9x + 5, com épsilon = 10^-2, no intervalo [2, 3]
bissec(2, 3, 10**-2, f)

