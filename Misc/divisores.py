
def divs(x):
	l = []
	for i in range(1, x):
		if int(x/i) == (x/i):
			l.append(i)
	return l

def alg(n, k):				# k - n' de iteracoes
	i=1
	print("Iniciando para n = {:d}".format(n))
	while(n != 0 and k <= 100):
		n = sum(divs(n))
		print("[{:d}] : {:d}".format(i, n))
		i+=1

alg(254838, 100)