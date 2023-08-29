
#include <iostream>
#include <ctime>
#include "estrutura.h"

using namespace std;

Celula *popular(Celula *lista, int n) {

  srand(time(NULL));
  
  for (int i = 0; i < n; i++) {
    lista = inserirLista(rand() % 100, lista);
  }
  return lista;
}
Celula *popular2(Celula *lista2, int n) {
  
  for (int i = 0; i < n; i++) {
    
    lista2 = inserirLista2(rand() % 100, lista2);
  }
  return lista2;
}

int main() {
  int qtdNumerosLista = 30;
  Celula *lista = NULL;
  Celula *lista2 = NULL;

  lista = popular(lista, qtdNumerosLista);
  cout << "" << endl;
  cout << "Lista 1" << endl;
  exibirLista(lista);

  lista2 = popular2(lista2, qtdNumerosLista);
  cout << "" << endl;
  cout << "Lista 2" << endl;
  exibirLista2(lista2);

  int numero;
  cout << "" << endl;
  cout << "Qual o número que você deseja apagar da lista? ";
  cin >> numero;

  lista = excluirLista(numero, lista);
  
  lista = excluirOcorrenciasLista(numero, lista);
  cout << "" << endl;
  cout << "Lista após exclusão" << endl;
  exibirLista(lista);

  juntaListas(lista,lista2);
  cout << "" << endl;
  cout << "As listas juntas:" << endl;
  
  exibirLista(lista);
 
  
  return 0;
}