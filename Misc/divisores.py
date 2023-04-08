from numba import jit, cuda
import numpy as np

@jit(target_backend='CPU')
def divs(x):
	l = []
	for i in range(1, int(x / 2) + 1):
		if x % i == 0:
			l.append(i)
	return l

def alg(n, k):				# k - n' de iteracoes
	i=1
	print(">> Iniciando para n = {:d}".format(n))
	while(n != 0):
		n = sum(divs(n))
		print("[{:d}] : {:d}".format(i, n))
		i+=1
		#if(n > 100000000):
		#	print(">> Interrupcao: Valor muito grande para computar")
		#	return 0

# 276, 552, 564, 660, and 966.
#alg(276, 100)
#alg(552, 100)
#alg(564, 100)
#alg(660, 100)
#alg(966, 100)

# Caso interessante
#alg(600, 100)

