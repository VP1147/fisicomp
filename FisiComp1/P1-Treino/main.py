# 1) (2,5 pontos) Partindo do código abaixo, faça as alteracões necessárias
# para apresentar na tela apenas os números ímpares entre 4 e 12.

x = 4
while 4 <= x <= 12:
	if x/2 != int(x/2): print(x)
	x += 1


#2) (2,5 pontos) Descreva o código a seguir e indique o resultado esperado.
# soma, sum = 0, 0
# for i in range(1,4):
# 	soma = soma + i
# 	sum = sum + i*2
# 	if sum>5:
# 		sum=sum + 2
# 	print (i)
# print (sum, soma)

# R: O código possui duas variáveis, soma e sum. Para cada interação do 
# loop 'for', para o intervalo de 1 a 4-1, à variável 'soma' é somada ao valor i
# (no qual é somado 1 em cada interação), enquanto que à variável 'sum' é
# somado o dobro de i. 
# Ao totalizar 5+1, à variável 'soma' passa a ser somado o valor 2. 
# Resultado esperado: Ao fim de cada interação, é impresso o valor de 'i' (1, 2 e 3), 
# e ao fim do loop 'for' é impresso o valor de 'sum' e 'soma' (16 e 6, respectivamente)

# Código corrigido
soma, Sum = 0, 0
for i in range(1,4):
	soma += i
	Sum += i*2
	if Sum > 5:
		Sum += 2
	print(i)
print (Sum, soma)


# 3) (2,5 pontos) Escreva um código em Python para calcular e escrever
# o valor de S, sendo S dado pela fórmula: S = 1 + 1/3 + 1/5 + ... + 1/99

S = 0
for i in range(1, 100):
	if i%2 != 0: 
		S += 1/i
print(S)


#5) (2,5 pontos) Faça um programa em Python que crie uma ou mais funções no código para calcular,
# numericamente, os valores da derivada de primeira ordem da função f(x)= x4 + x2 - 5,
# usando a definição matemática de derivada. Determine os valores das derivadas calculadas
# no intervalo x=[-1,3] com x variando em 0,1. Apresente os resultados para cada valor de x 
# em colunas, contendo: os valores de x e das derivadas de primeira ordem de f(x).

def f(x):								# f(x) = x⁴ + x² - 5
	return x**4 + x**2 - 5

def df(x): 								# df(x)/dx
	h = 0.0001							# lim x -> 0 
	return (f(x+h)-f(x))/h 				

i = -1
while i <= 3:
	print("x: "+str(round(i, 4))+" | f(x): "+str(round(f(i), 4))+
		" | df(x)/dx: "+str(round(df(i), 4)))
	i += 0.1

