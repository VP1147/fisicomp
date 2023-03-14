from math import sqrt

## Calcular o tempo de queda de um objeto

def TQueda(DeltaX):

	Ag = 9.81	# Ac. gravitacional (m/s²)
	t = (DeltaX/(Ag/2))**(1/2)

	return t
print(TQueda(100))
print(TQueda(25))

## Deterninar de um n° é par ou ímpar

def IsEven(n):
	if n/2 == int(n/2): return True
	else: return False

print(IsEven(11))
print(IsEven(4))

## Calcular a energia necessária para aquecer gelo até uma dada temperatura.

def GeloQuente(m, Tf, Ti): 		## Massa - Kg
	DeltaT = Tf-Ti 				## Temp. - Kelvin
	Q = m*2110*DeltaT
	print(Q/1000, "kJ")

def rel(x,y):
	if x == y:
		print("Equal")
	elif x < y:
		prinf("Less")
	else:
		print("Greater")

def CtoF(Tc):
	Tf = 1.8*Tc + 32
	print(Tf)
	if Tc > 40: 	
		print("Muito quente")
	elif Tc >= 30: 	
		print("Quente")
	elif Tc >= 15:	
		print("Agradável")
	elif Tc >= 5:
		print("Friozinho")
	elif Tc >= 0:
		print("Frio")
	elif Tc >= -10:
		print("Muito frio")
	elif Tc < -10:
		print("Congelante")

def Notas(n):
	if n >= 9.0:
		return "A"
	elif n >= 8.0:
		return "B"
	elif n >= 7.0:
		return "C"
	elif n >= 6.0:
		return "D"
	elif n < 6.0:
		return "F"
	else: 
		print("Score incorreto")
		return 0

def Bhaskara(a,b,c):
	Delta = (b**2)-(4*a*c)
	x1 = ((b*-1)+sqrt(Delta))/(2*a)
	x2 = ((b*-1)-sqrt(Delta))/(2*a)

	return x1, x2

def Salario():
	sal = 0
	try:
		hs = int(input("Horas: "))
		salhs = float(input("Salário/hora: "))
	except:
		return "Valor inválido"

	for i in range(0,hs):
		if i >= 40:
			sal += salhs*1.5
		else:
			sal += salhs
	return sal