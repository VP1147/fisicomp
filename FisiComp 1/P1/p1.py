### P1 - Física Computacional 1
### Aluno: Vinícius A. Pavão
### Curso: Engenharia Física - UFMS

# External libraries
import math as m

## 1) (3,0 pontos) Faça um código em Python para calcular a altura
# máxima, o alcance máximo e o tempo de subida num lançamento oblíquo*.

def obliquo(vo):
	a = 45 							# Lançamento obliquo: 45°
	g = 9.81

	# Componentes
	vox = vo*m.cos(a)
	voy = vo*m.sin(a)

	# Calculando os valores

	hmax = ((vo**2)*(m.sin(a)**2))/(2*g)
	amax = ((vo**2)*m.sin(2*a))/g
	t = voy/g

	# Imprimindo os valores
	print("Para Vo = "+str(vo)+"m/s")
	print("Altura máxima: "+str(round(hmax, 2))+"m")
	print("Alcance máximo: "+str(round(amax, 2))+"m")
	print("Tempo de subida: "+str(round(t, 2))+"s")

# Velocidades de exemplo

obliquo(10)
obliquo(36)

## 2) (3,0 pontos) Escreva um código em Python para calcular e escrever
# o valor de S, sendo S dado pela fórmula: S = 1 + 1/3² + 1/5² + 1/9² +
# 1/11² + 1/13² + 1/15² + 1/19². Utilize uma estrutura de repetição 
# (for ou while) para calcular S.

s = 0 
for i in range(0, 19):
	if i % 2 != 0: s += 1/(i**2)

print(s)

## 3) Considere o polinômio p(x)=x³ + 3x² – 5x. 

def p(x):
	return x**3 +3*x**2 -5*x

# Faça um programa em Python que crie uma ou mais funções 
# no código para:

# a) (2,0 pontos) apresentar na tela os valores de x e p(x) 
# no intervalo x=[0,2] com x variando de 0,1 em 0,1.

x = 0
while x <= 2:
	print("x =", round(x, 2), "| p(x) =", round(p(x), 3))
	x += 0.1

# b) (2,0 pontos) apresentar na tela os valores de x e p'(x) 
# no intervalo x=[0,2] com x variando de 0,1 em 0,1, onde
# p'(x) é a derivada numérica de primeira ordem de p(x) e pode
# ser calculada usando p'(x) = f(x+h) − f(x)/h com valor de h 
# bem pequeno (p.ex.: h = 0,001).

def df(f, x):                            # Recebe f(x) e x.
										 # Retorna a derivada de f
										 # no ponto x (df/dx).
	h = 0.001
	return (f(x+h)-f(x))/h

x = 0
while x <= 2:
	print("x =", round(x, 2), "| p'(x) =", round(df(p, x), 3))
	x += 0.1
