#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

#include "arvores.h"

void popularDoArquivo(Arvore ** raiz) {
    char nomeArquivo[200];
    ifstream procurador;
    
    cout << "informe o arquivo que deseja abrir: ";
    cin >> nomeArquivo;
  
    procurador.open(nomeArquivo);
    if (!procurador) {
        cout << "Arquivo digitado nao localizado!";
        return;
    }
    string linha;
    string valor;
    
    int posicaoEspaco = 0;
    while (getline(procurador,linha)){ 
      posicaoEspaco = linha.find(" ");
    
      valor = linha.substr(0,posicaoEspaco);
      *raiz = inserir(stoi(valor), *raiz);      
    } 
    procurador.close();
  }
int main() {
    Arvore *raiz = NULL;

    popularDoArquivo(&raiz);

    exibir(raiz,0);

  
    cout << "Menor valor: " << menorElemento(raiz)->valor << endl;

    cout << "Maior valor: " << maiorElemento(raiz)->valor << endl;
  
    int numero = menorElemento(raiz)->valor;
    int numeromaior = maiorElemento(raiz)->valor;
  
    cout << numero << " estah no nivel: " << localizarNivel(numero, raiz) << endl;

    cout << numeromaior << " estah no nivel: " << localizarNivel(numeromaior, raiz) << endl;
    cout <<"o maior valor e o menor valor estão no mesmo nivel sim(0) ou não(1): ";
    cout <<localizarNivelmaioremenor(numero,raiz) << endl;
    return 1;

}