## FÍSICA COMPUTACIONAL E INFORMÁTICA
## INTEGRAÇÃO NUMÉRICA
## REVISÃO PARA PROVA – MÉTODO de 3/8 de SIMPSON
## ALUNO: Vinicius Pavao

# Implemente um código em Python para o Método de 3/8 de Simpson e calcule a
# integral:
# 	3
# 	∫ 1/x dx
# 	1
# Compare o resultado numérico com a resposta analítica: ln(3)−ln(1)

import math as m

def simpson38(f, a, b, n):		# Integral de f(x) dx no intervalo [a, b]
	i = 0  						# Contador de iteracoes
	d = a
	h = (b-a)/(3*n)				# Dividindo os subintervalos
	S = 0						# Variavel de soma
	while(i <= n-3):
		try: S += f(d) + 3*f(d+h) + 3*f(d+2*h) + f(d+3*h)
		except: pass
		d += 3*h
		i += 1
	S = S*((3*h)/8)

	#print("I ~= {:.12f}".format(S))
	return S

# Funcao f(x) = 1/x
def f(x):
	return 1/x

# Calculando a integral de f(x) pela regra de 3/8 de Simpson com
# 1000 iteracoes
Sp = simpson38(f, 1, 3, 1000)

# Pelo metodo analitico
Al = m.log(3) - m.log(1)

print("I_S ~= {:.12f}".format(Sp))
print("I_A = {:.12f}".format(Al))
print("Erro = {:.12f}%".format(((Sp-Al)/Sp)*100))