import math

def MenorNCedulas(v): # v - Valor

		# 	Escreva um código que retorne o menor número de cédulas necessárias para
		# representar um valor que se quer sacar de um caixa eletrônico. As cédulas
		# disponíveis são de R$ 200, R$ 100, R$ 50 e R$ 20. Quando não for possível sacar o
		# valor desejado, mencionar na tela "Não disponível nesse valor".

	vf = 0
	n200 	= 0
	n100 	= 0
	n50 	= 0
	n20 	= 0
	loop 	= True

	while loop == True:
		if vf+200 <= v: 
			vf += 200
			n200 += 1
		elif vf+100 <= v:
			vf += 100
			n100 += 1
		elif vf+50 <= v and vf+50+20 <= v:
			vf += 50
			n50 += 1
		elif vf+20 <= v:
			vf += 20
			n20 += 1
		else:
			if vf != v: 
				print("Não disponível nesse valor\n")
				loop = False
			elif vf == v:
				print(n200,"notas de R$200")
				print(n100,"notas de R$100")
				print(n50,"notas de R$50")
				print(n20,"notas de R$20\n")
				loop = False

MenorNCedulas(150)
MenorNCedulas(870)
MenorNCedulas(610)
MenorNCedulas(60)

def Deriv(n,x): # f(x) = x^n
	print("f(x) = "+str(x)+"x^"+str(n))
	print("d/dx = "+str(x*n)+"x^"+str(n-1))

Deriv(2, 5)
Deriv(3, 8)

def Maior(n1, n2, n3, n4, n5):
	nm = 0
	n = [n1, n2, n3, n4, n5]
	for i in range(0, len(n)):
		if n[i] > nm: nm = n[i]
	print(nm)

Maior(1, 15, 10, 5, 18)

def lim(n):
	t = 0
	for i in range(1, n):
		t += 1/i
	print("1 + 1/2 + 1/3 + ... + 1/"+str(n)+" = "+str("{:.3f}".format(t)))

lim(100)
lim(20)
lim(5)

def DistPontos(xo, yo, xf, yf):
	d = math.sqrt( (xf-xo)**2 + (yf-yo)**2 )
	print("Distância entre ("+str(xo)+", "+str(yo)+") e ("+str(xf)+", "+str(yf)+"): {:.3f}".format(d))

DistPontos(1, 2, 2, 1)
DistPontos(3, 4, 1, 2)

def ParImpar(n):
	if n/2 == int(n/2): print(n, "é par")
	else: print(n, "é ímpar")

ParImpar(2)
ParImpar(5)
ParImpar(1)

def Desloc(v, DeltaT):
	d = v*DeltaT
	print(d)

def Balist(vo, ang):
	g = 9.81
	h = ( vo**2 * math.sin(ang)**2 ) / (2*g)
	s = ( vo**2 * math.sin(ang*2) ) / g
	t = ( vo * math.sin(ang) ) / g

	print("Lançamento de "+str(ang)+"° com Vo = "+str(vo)+"m/s :")
	print("Altura máx: "+str(round(h, 3))+"m")
	print("Deslocamento: "+str(round(s, 3))+"m")
	print("Tempo em queda: "+str(round(t, 3))+"s")

Balist(15, 45)

# Função original

# def distPontos(x1, y1, x2):
# 	 distX == (x2 - x1) * 2
#	 distY == (y2 - y1) ** 2
#	 dist = (distX + distY) * (0.5)
#	 return dist

# Função com "bugs" corrigidos
def distPontos(x1, y1, x2, y2):
	distX = (x2 - x1) ** 2
	distY = (y2 - y1) ** 2
	dist = (distX + distY) ** (0.5)
	return dist

print(distPontos(1, 2, 2, 1))


# 8) Usando comandos de laços, funções, condicionais, entre outros, escreva um
# programa para resolver algum problema relacionado à Física.

def DerivPol(n, x): 	# Recebe monômio do tipo xt^n
	return (x*n, n-1)	# Retorna d/dt = n*x^(n-1)

# Problema: Uma partícula se move de tal forma que
# a posição (m) em função do tempo (s) é dada por
# r = i +4t²j + tk. Escreva expressões para a velocidade
# e a aceleração em função do tempo.

# Divide-se a equação em 3 monômios (i, j, k), onde cada monômio
# é dado em x e n, tal que x*t^n

S = [[1, 0],[4, 2],[1, 1]] 	# i +4t²j + tk
Coord = ['i','j','k']		# Vetores unitários

# Posição (dada pelo problema):
print("S = i + 4t²j + tk")

# Velocidade (dS/dt):

V = [0,0,0]

for i in range(0, 3):
	V[i] = DerivPol(S[i][1], S[i][0]) # Calcula a derivada do monômio

print(str(V[0][0])+"t^"+str(V[0][1])+
	"î + "+str(V[1][0])+"t^"+str(V[1][1])+
	"ĵ + "+str(V[2][0])+"t^"+str(V[2][1])+"k")

# Aceleração (dV/dt):

A = [0,0,0]

for i in range(0, 3):
	A[i] = DerivPol(V[i][1], V[i][0])

print(str(A[0][0])+"t^"+str(A[0][1])+
	"î + "+str(A[1][0])+"t^"+str(A[1][1])+
	"ĵ + "+str(A[2][0])+"t^"+str(A[2][1])+"k")

# Teste: Derivada de função declarada

def f(x):
	return 2*x**2

def df(dx):
	h = 0.0001
	return (f(x+h)-f(x))/h
