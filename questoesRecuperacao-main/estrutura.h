#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

//struct utilizado tanto pra pilha quanto pra lista
typedef struct no {
  int dado;
  struct no *prox;
} Celula;

//mostra os valores ordenados, do menor ao maior
void exibirLista(Celula *lista) {
  Celula *p;
  for (p = lista; p; p = p->prox) {
    cout << p->dado << endl;
  }
}

Celula *inserirListaControleDuplicados(int valor, Celula *lista) {
  //alocar memoria
  Celula *novo = (Celula*)malloc(sizeof(Celula));

  //depositar valores
  novo->dado = valor;
  novo->prox = NULL;

  //percorrer para encontrar o local adequado na lista
  //testar se é a primeira vez
  if (!lista) return novo;

  Celula *p, *pR;
  for (pR = NULL, p = lista; p; pR = p, p = p->prox) {
    if (valor < p->dado) break;

    if (valor == p->dado) return lista; //valor ja cadastrado, logo retorna a lista sem alteração
  }

  //é o primeiro
  if (p == lista) {
    novo->prox = lista;
    return novo;
  }
  //é o último
  if (!p) {
    pR->prox = novo;
  } else { //está no meio de duas celulas
    pR->prox = novo;
    novo->prox = p;
  }
  //retorna o inicio da lista
  return lista;  
}

Celula *inserirListaSemControleDuplicados(int valor, Celula *lista) {
  //alocar memoria
  Celula *novo = (Celula*)malloc(sizeof(Celula));

  //depositar valores
  novo->dado = valor;
  novo->prox = NULL;

  //percorrer para encontrar o local adequado na lista
  //testar se é a primeira vez
  if (!lista) return novo;

  Celula *p, *pR;
  for (pR = NULL, p = lista; p; pR = p, p = p->prox) {
    if (valor < p->dado) break;
  }

  //é o primeiro
  if (p == lista) {
    novo->prox = lista;
    return novo;
  }
  //é o último
  if (!p) {
    pR->prox = novo;
  } else { //está no meio de duas celulas
    pR->prox = novo;
    novo->prox = p;
  }
  //retorna o inicio da lista
  return lista;  
}

//metodo que receba um valor, o localiza na lista e o remove da estrutura
Celula *excluirLista(int valor, Celula *lista) {
  Celula *p, *pR;

  if (!lista) {
    cout << "Lista vazia. Operação cancelada!" << endl;
    return lista;
  }

  for (pR = NULL, p = lista; p; pR = p, p = p->prox) {
    if (valor == p->dado) {
      //eh o primeiro
      if (p == lista) {
        lista = lista->prox;
      } else if (!p->prox) { //eh o ultimo
        pR->prox = NULL;
      } else { //esta entre celulas
        pR->prox = p->prox;
      }
      free(p);
      return lista;
    }
  }
  cout << "Valor não localizado para exclusão!" << endl;
  return lista;
}

Celula *excluirOcorrenciasLista(int valor, Celula *lista) {
  Celula *p, *pR;
  int contaExcluidos = 0;

  if (!lista) {
    cout << "Lista vazia. Operação cancelada!" << endl;
    return lista;
  }

  bool houveExclusao;
  do {
    houveExclusao = false;
    for (pR = NULL, p = lista; p; pR = p, p = p->prox) {
      if (valor == p->dado) {
        contaExcluidos++; //toda vez que localiza, prepara para excluir, mas antes conta
        //eh o primeiro
        if (p == lista) {
          lista = lista->prox;
        } else if (!p->prox) { //eh o ultimo
          pR->prox = NULL;
        } else { //esta entre celulas
          pR->prox = p->prox;
        }
        free(p);
        houveExclusao = true;
        break;
      }
    }   
  } while (houveExclusao);

  cout << "O total de excluidos foi: " << contaExcluidos << endl;
  return lista;
}

Celula *excluirparesLista( Celula *lista) {
  Celula *p, *pR;

  if (!lista) {
    cout << "Lista vazia. Operação cancelada!" << endl;
    return lista;
  }
  bool houveExclusao;
  do {
    houveExclusao = false;
    for (pR = NULL, p = lista; p; pR = p, p = p->prox) {     
        //eh o primeiro
        if(p->dado % 2 == 0){
            if (p == lista) {
              lista = lista->prox;
            } else if (!p->prox) { //eh o ultimo
              pR->prox = NULL;
            } else { //esta entre celulas
            pR->prox = p->prox;
          }
          
        free(p);
        houveExclusao = true;
        break;
      }
    }   
  } while (houveExclusao);
  return lista;
}
//metodo que recebe uma lista e retorna a quantidade de elementos
int contarElementos(Celula *lista) {
  int contador = 0;
  Celula *p;
  for (p = lista; p ; p = p->prox) {
    contador++;
  }
  return contador;
}

void verificarPresenca(Celula *lista1, Celula* lista2) {
  if (!lista1 || !lista2) {
    cout << "Operação não realizada, pois ambas não existem ou uma delas também não existe!" << endl;
    return ;
  }

  Celula *p1, *p2;

  for (p1 = lista1; p1; p1 = p1->prox) {
    for (p2 = lista2; p2; p2 = p2->prox) {
      if (p1->dado == p2->dado) {
        cout << "Este dado ocorre nas 2 listas: " << p1->dado << endl;
      }
    }
  }  
}

Celula *unirListas(Celula *lista1, Celula *lista2) {
  if (!lista1 || !lista2) {
    cout << "Operação não realizada, pois ambas não existem ou uma delas também não existe!" << endl;
    return NULL;
  }

  Celula *p;
  
  for (p = lista1; p->prox; p = p->prox);

  p->prox = lista2;

  return lista1;
}

float media(Celula *lista){
  int maiorValor;
  int menorValor;
  float media;
  Celula *p;
  for (p = lista; p; p = p->prox) {
    maiorValor = p->dado;
  }
  for (p = lista; p; p->prox = p) {
    menorValor = p->dado;
  }
  media = (menorValor + maiorValor) / 2;

  return media;
}

void exibirListametade(Celula *lista) {
  if (!lista) {
    cout << "Operação não realizada, lista não existe" << endl;
    return ;
  }
  Celula *p;
  int qtdelementos = contarElementos(lista);
  int i ;
  for(p = lista ,i = 0 ; i < (qtdelementos%2) ;i++, p = p->prox){
    cout << "ola" << endl;
    cout << p->dado << endl;
  }
}


