#include <iostream>
#include <vector>
#include <math.h>
#include <time.h>
#include "Header.h"

using namespace std;

int main() {

	int numind = 20;
	int longitud = 10;
	float mutacion = 0.02;

	srand(time(NULL));
	
	poblacion P;
	P.generarpoblacion();
	submitGen(P);

	for (int i = 1; i <= 50; i++) {
		cout << endl << endl << "Generación " << i << endl;
		poblacion x = heredar(TOTAL[i-1]);
		x.orden();
		for (individuo z : x.padres) {
			cout << "{"; z.showind(); cout << "} ";
		}
		cout << endl;
		for (individuo k : x.generacion) {
			cout << "[ "; k.showind(); cout << ", " << k.numero() << "  Fitness: " << k.fitness << " ]" << endl;
		}
		submitGen(x);
	}

	system("PAUSE");

	return 0;
}
