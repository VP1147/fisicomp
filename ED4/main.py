import tg.tg as tg				# https://github.com/VP1147/tg/blob/master/tg.py 
from getch import getch

tg.theme("tg/dark.json")
tg.init(800, 25, 1)

def f(x):
	return x**3 -9*x + 3

global k
def df(x): 								# df/dx
	h = 0.0001							# lim x->0 
	return (f(x+h)-f(x))/h
	

def tangent(x):							# # y = m(x-a) + f(a)
	m = df(x)
	return m*(x-k) + f(k)

p = 0.1
interval = [-2, 2]

tg.plot(f)

k = interval[0]
while k <= interval[1]:
	tg.plot(tangent, [0, 50, 50])		# Tip: Varies the colour for each tangent line
	k += p

getch()