import math as m

def f(x):
	return m.e**x

def yh(x, y):
	return -1.2*y + 7*m.e**(-0.3*x)

def euler(f, h, yi, xf):
	xi = 0

	x = xi
	y = yi
	X = []
	Y = []
	while x <= xf :
		ya = f(x)
		dp = 100*(ya - y)/ya
		print("x = {:.2f} | y = {:.4f} | ya = {:.4f} | dp = {:.4f}%".format(x, y, ya, dp))
		Y.append(y)
		X.append(x)
		x += h
		y += h*yh(x, y)
	return X, Y

import matplotlib.pyplot as plt
import numpy as np

xf = 7.01
yi = 3

X, Y = euler(f, 0.1, yi, xf)
#Ya = m.e**X

fig = plt.figure()
plt.plot(X,Y, 'r')
#plt.plot(X, Ya, 'r')
plt.show()
