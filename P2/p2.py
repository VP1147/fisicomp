### P1 - Física Computacional 1
### Aluno: Vinícius A. Pavão
### Curso: Engenharia Física - UFMS

# External libraries
import math as m

# Seja f(x) contínua num intervalo [a, b] 
# e tal que existe apenas uma única raiz no intervalo.

## 1) Utilizando os Métodos da Posição Falsa e de Newton-Raphson, 
# encontre a raiz da função f(x) = x⁴ – 3x² + 2x – 5 no intervalo [0;3]. 
# Para isso, utilize ε1 = ε2 = 10^-4 como critérios de parada ou k > 100.


# Definindo a função f(x)
def f(x):
	return x**4 -3*x**2 +2*x -5

# a) (5,0 pontos) Implemente apenas um código em Python que utiliza os dois métodos
# mencionados acima;

# Definindo o método da posição falsa (ED5)
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
		 
		print("{:3d} {:.6f} {:.6f}".format(i, chi, f(chi)))
		chi = (a+b)/2
		if i > 100: 						# Critério de parada k > 100
			#print(">> Limite de Iterações")
			return a, b, chi, f(chi)
		i+=1
	print("{:3d} {:.6f} {:.6f}".format(i, chi, f(chi)))

# Definindo o método de Newton-Raphson
def df(x):								# Derivada de f(x) dx

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

# b) (5,0 pontos) Faça o código escrever na tela: o seu nome (na primeira linha) 
#e os valores de k, xk, f(xk) das iterações.

# Imprime o nome
print("Vinícius Arruda Pavão\n")

# Imprime o retorno de cada método
posfs(0, 3, 10**-4, f)
newton(0, 3, 10**-4, f, df)
