import latexify
import math

@latexify.function
def delta(a,b,c):
	return b**2 -4*a*c
delta

@latexify.function
def solve(a, b, c):
    return (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)

solve