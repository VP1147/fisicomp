def d(x):
	l = []
	for i in range(1, int(x / 2) + 1):
		if x % i == 0:
			l.append(i)
	return sum(l)

def dk(x):
	i=1
	print(">> Iniciando para n = {:d}".format(x))
	while(x != 0):
		x = d(x)
		print("[{:d}] : {:d}".format(i, x))
		i+=1

		#if(n > 100000000):
		#	print(">> Interrupcao: Valor muito grande para computar")
		#	return 0

# 276, 552, 564, 660, and 966.
#alg(8400)
#alg(552, 100)
#alg(564, 100)
#alg(660, 100)
#alg(966, 100)

# Caso interessante: volta em 601
dk(600)

# Caso interessante: Numero sociavel
#alg(12496)
#dk(576)


