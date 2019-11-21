#pragma once
#ifndef header_h
#define header_h

#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

int aleatorio(int inicio, int fin);

int numindiv = 20; //num individuos
int longitud = 10; //Cantidad de genes de los individuos
int mutacion = 2; // Porcentaje de mutuacion

class individuo {
public:
	float fitness = 0;
	vector<bool> genes;
	double valor = 0;

	double numero() {
		double numero = 0;
		bool signo = genes[0];
		int entero = genes[1] * 4 + genes[2] * 2 + genes[3] * 1;
		numero += entero;

		double fraccionaria = 0;
		for (int i = 4; i < longitud; i++) {
			fraccionaria += genes[i] * pow(2, - i + 3);
		}
		
		numero += fraccionaria;

		if (signo)
			numero *= -1;

		this->valor = numero;
		this->fitness = numero * numero;
		return numero;

	};

	void showind() {
		for (bool gen : genes) {
			cout << gen;
		};
	}

	bool operator < (individuo i2)	{
		return (fitness < i2.fitness);
	}
};

individuo generarindividuo() {
	individuo res;
	for (int i = 0; i < longitud; i++) {
		bool temp;
		temp = aleatorio(0, 1);
		res.genes.push_back(temp);
	}
	res.numero();
	return res;
}

individuo crossover(individuo i1, individuo i2) {
	individuo child;
	for (int i = 0; i < longitud; i++) {
		if (aleatorio(1, 2) == 1) {
			child.genes.push_back(i1.genes[i]);
		}
		else {
			child.genes.push_back(i2.genes[i]);
		}
	}
	child.numero();
	return child;
}

void mutar(individuo& i) {
	for (bool g : i.genes) {
		int random = aleatorio(0, 100);
		if (random <= mutacion)
			g = !g;
	}
}

class poblacion {
public:
	vector<individuo> padres;
	vector<individuo> generacion;
	bool convergencia;

	void generarpoblacion()
	{
		for (int i = 0; i < numindiv; i++) {
			generacion.push_back(generarindividuo());			
		}
	};

	void mostrarpob() {
		cout << "{";
		for (individuo i : this->generacion) {
			i.showind(); cout << ", ";
		}
		cout << "}";
	}

	void orden() {
		sort(generacion.begin(), generacion.end());
	}

};

vector<individuo> seleccion(poblacion p) {
	vector<individuo> res;
	for (int i = 0; i < numindiv / 4; i++) {
		res.push_back(p.generacion[i]);
	}
	for (int i = 0; i < numindiv / 4; i++) {
		res.push_back(p.generacion[aleatorio((numindiv / 4), numindiv-1)]);
	}
	return res;
}

poblacion heredar(poblacion p) {
	poblacion nueva;
	nueva.padres = seleccion(p);
	for (int i = 0; i < numindiv; i++) {
		individuo father = nueva.padres[aleatorio(0, nueva.padres.size() - 1)];
		individuo mother = nueva.padres[aleatorio(0, nueva.padres.size() - 1)];
		individuo child = crossover(father, mother);
		nueva.generacion.push_back(child);
	}

	for (individuo x : nueva.generacion) {
		mutar(x);
		x.numero();
	}
	return nueva;
}

vector<poblacion> TOTAL;

void submitGen(poblacion asubir) {
	TOTAL.push_back(asubir);
}

int aleatorio(int inicio, int fin) {
	int randNum = rand() % (fin - inicio + 1) + inicio;
	return randNum;
};

#endif
