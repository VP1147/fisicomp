## Projeto Final de disciplina
## Curso: Física Computacional I
## Aluno: Vinícius A. Pavão

# Problema: Tempo de queda (t) de um objeto pontual sobre outro de massa M e e raio R,
# a partir de uma distância D de seu centro.

import math as m

def Queda(M, R, D):
	G = 6.67*(10**-11) 		# Constante gravitacional
	Ac = (G*M)/(D+R)**2		# Ac. grav. do objeto
	t = m.sqrt((2*D)/Ac)	# Tempo de queda
	V = Ac*t
	return Ac, t, V

M = float(input("Massa do objeto grande (Kg): "))
R = float(input("Raio do objeto grande (m): "))
D = float(input("Distância da superfície (m): "))

Ac, t, V = Queda(M, R, D)

print("Aceleração (m/s²):", Ac)
print("Tempo de queda (s):", t, ", ou seja,", t/3600, "horas")
print("Velocidade da queda (m/s):", V)
