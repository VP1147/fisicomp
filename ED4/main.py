import math
import tg
from getch import getch

tg.theme("dark.json")

# f(x) = x²
def f(x):
	return math.sin(x)

i = [-10, 10]			# Intervalo de busca
p = 1/100				# Período
x = i[0]
l = []
while x <= i[1]:
	#print("x:",round(x, 2),"| f(x):",round(f(x), 2))
	if f(x-p)*f(x) < 0:
		print("--> Raiz entre", round(x, 2), "e",round(x-p, 2))
		tg.Mkrs.append(round(x, 3))
	x += p

print(tg.Mkrs)
tg.init(800, 20, math.pi)
tg.plot(f)

getch()