## Operações Simples
a = 9-((1+2)/3)
b = 9-1+(2/3)
c = 9+(1*2)-3
d = 9+(1*2)-3
e = 9*(2/3)
f = [10*3.9, 50*3.9, 100*3.9] ## Tupla
print(a, b, c, d, e, f)

## Exponenciação
g = [2**3, 3**2, 4**5]

## Resto de divisões
h = [10 % 3, 16 % 7, 63 % 8]

print(g, h)

## Operadores relacionais
a = 1
b = 2

print(	a == 2,
		a == 1,
		a >= 1,
		a > 1,
		b == 3,
		a > b,
		a < b,
		a == b,
		a != b)

x = 1
y = 0

print(x >= 2 and y != 0 and (x/y) > 2)
print(x >= 2 and (x/y) > 2 and y != 0)


## Código Python de notas de Física Computacional

nota1 = 8.0
nota2 = 9.2
nota_trabalhos = 7.8

media_notas = (nota1+nota2)/2
media_final = (media_notas*3 + nota_trabalhos)/4

print(media_final)
if media_final > 6.0: print("Aprovado")
else: print("Reprovado")


## Operadores lógicos

print(
		not True,
		not False,
		True and True,
		True and False,
		False and False,
		True or True,
		True or False,
		False or False)


## Código Python para verificar notas e faltas

nota_final = 7.8
faltas = 25
aprovado = nota_final > 6 and faltas <= 16
print(aprovado)
faltas =10
print(aprovado)
aprovado = nota_final > 6 and faltas <= 16
print(aprovado)


## Formatando a saída na tela
print ("%5f" 	% 5)
print ("%5.2f" 	% 5)
print ("%6.2f" 	% 5)
print ("%6.3f" 	% 5)
a, b = 1, 2
print ("%d + %d = %d" % (a, b, a+b))
print ("%f + %f = %f" % (a, b, a+b))
print ("%5.2f + %5.2f = %5.2f" % (a, b, a+b))
a, b = 1.5, 2.2
print ("%d + %d = %d" % (a, b, a+b))
print ("%f + %f = %f" % (a, b, a+b))

# Adendum: eu, particularmente, acho mais eficiente 
# utilizar a função str() para concatenar variáveis
# numéricas na função print().


## Código passeio do Shopping:
divida = 0
compra = 100
divida += compra 	# Mais eficiente que usar
						# divida = divida + compra
print(divida)
compra = 50
divida += compra
print(divida)
compra = 300
divida += compra
print(divida)