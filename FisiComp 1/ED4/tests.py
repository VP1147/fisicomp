import math
import tg
from getch import getch

tg.theme("dark.json")

def f(x):
	return x % math.pi*1/4*x

i = [-10, 10]			# Intervalo de busca
p = 1/100							# Período
x = i[0]
l = []
while x <= i[1]:
	#print("x:",round(x, 2),"| f(x):",round(f(x), 2))
	if f(x-p)*f(x) < 0:
		print("--> Raiz entre", round(x, 2), "e",round(x-p, 2))
		tg.Mkrs.append(round(x, 3))
	x += p

print(tg.Mkrs)
tg.init(800, 20, 1)
tg.plot(f)

getch()