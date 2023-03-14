## DESAFIO CÓDIGO PYTHON - Valor a ser pago para um funcionário

# Escreva um programa em Python para pedir o número de horas trabalhadas
# e o salário por hora de um funcionário. Depois, calcule o valor a ser 
# pago para o funcionário. O salário por hora aumenta em 50% para as horas 
# que extrapolarem 40 horas trabalhadas. Para testar o programa, vamos usar: 
# 45 horas trabalhadas com salário por hora de 10.50. Use "input" para ler os 
# valores em strings e "float" para convertê-las em números. O resultado para
# o valor a ser pago deve ser 498.75. Não esqueça de escrever esse valor na
# tela usando o "print".

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

Salario()