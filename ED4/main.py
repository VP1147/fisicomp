import math

# Encontra as raízes 
def f(x):
	return x**2

i = [-10, 10]
interactions = 4

for n in range(1, interactions+1):
	p = math.sqrt(i[0]**2 +i[1]**2)/10		# Período
	x = i[0]
	print("--> Interação:", n, "- i:", i, "- p:", p)
	while x <= i[1]:
		# print(x)
		if f(x-p)*f(x) < 0:
			r += 1
			print("--> Raiz entre", round(x, 2), "e",round(x-p, 2))
			i = [x-p, x]
			# print("x:",round(x, 2),"| f(x):",round(f(x), 2))
		x += p
