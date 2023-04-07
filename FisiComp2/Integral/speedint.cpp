#include <iostream>
#include <cmath>

using namespace std;

void integral(int a, int b, double (*f)(double)) {
	int n = pow(10,1); double S; int k = 1; double i = a; double deltax = ((b-a)/n);
	while(k <= n) {
		i += deltax;
		cout << i;
		S += f(i)*deltax;
		k+=1;
	}
	printf("n = %d\n", n);
	printf("S = %4f\n", S);
}

double f(double x) {
	return pow(x,2);
}
int main(void){
	integral(0, 1, &f);
}