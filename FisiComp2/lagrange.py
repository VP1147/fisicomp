# Interpolacao pelo metodo de Lagrange

def Lk(x, k, n, xk = []):
	j = 0
	L = 1
	while j <= n:
		if j != k:
			L *= (x - xk[j]) / (xk[k] - xk[j])
		j += 1
	return L

def lagrange(x, n, xk = [], yk = []):

	P = 0
	k = 0
	while k <= n:
		P += yk[k] * Lk(x, k, n, xk)
		print("k={:d}		xk={:.2f}	Lk={:.2f}".format(k, xk[k], Lk(x, k, n, xk)))
		k += 1
	print(P)
	return P

xk = [-1, 0, 2]
yk = [4, 1, -1]

lagrange(0, 2, xk, yk)


import matplotlib.pyplot as plt

xi = -3
xf = 4
yi = 0
X = []
Y = []

n = 2

h = 0.1 								# Densidade do gráfico
while xi < xf: 
	X.append(xi)
	Y.append(lagrange(xi, n, xk, yk))
	xi += h
	yi += h


fig = plt.figure()

plt.scatter(xk, yk)
plt.plot(X, Y)

plt.grid()
plt.show()