# Interpolacao pelo metodo de Lagrange

def Lk(x, k, n, xk = []):
	j = 0
	L = 1
	while j <= n:
		if j != k:
			L *= (x - xk[j]) / (xk[k] - xk[j])
		j += 1
	return L

def lagrange(x, xk = [], yk = []):

	P = 0
	k = 0
	n = 2
	while k <= n:
		P += yk[k] * Lk(x, k, n, xk)
		print("k={:d}		xk={:.2f}	Lk={:.2f}".format(k, xk[k], Lk(x, k, n, xk)))
		k += 1
	print(P)
	return P

xk = [20, 25, 30]
yk = [0.99907, 0.99852, 0.99826]

lagrange(25, xk, yk)


import matplotlib.pyplot as plt

xi = 15
xf = 35
yi = 0
X = []
Y = []
while xi < xf: 
	X.append(xi)
	Y.append(lagrange(xi, xk, yk))
	xi += 1
	yi += 1


fig = plt.figure()

plt.scatter(xk, yk)
plt.plot(X, Y)

plt.grid()
plt.show()