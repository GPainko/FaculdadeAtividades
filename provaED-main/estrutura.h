#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;


typedef struct no {
  int dado;
  struct no *prox;
} Celula;


void exibirPilha(Celula *topo) {
  Celula *p;
  for (p = topo; p; p = p->prox) {
    cout << p->dado << endl;
  }
}

Celula *inserirPilha(int valor, Celula *topo) {
  
  Celula *novo = (Celula*)malloc(sizeof(Celula));

  novo->dado = valor;

  novo->prox = topo;
  
  return novo;
}

void exibirLista(Celula *lista) {
  Celula *p;
  for (p = lista; p; p = p->prox) {
    cout << p->dado << endl;
  }
}

Celula *inserirLista(int valor, Celula *lista) {
  
  Celula *novo = (Celula*)malloc(sizeof(Celula));

  novo->dado = valor;
  novo->prox = NULL;
  Celula *p, *pR;

  if (!lista) return novo;

  for (pR = NULL, p = lista; p; pR = p, p = p->prox) {
    if (valor == p->dado) {
      
      if (p == lista) {
        lista = lista->prox;
      } else if (!p->prox) { 
        pR->prox = NULL;
      } else { 
        pR->prox = p->prox;
      }
      free(p);
      return lista;
    }
  }
  for (pR = NULL, p = lista; p; pR = p, p = p->prox) {
    if (valor < p->dado) break;
  }

  if (p == lista) {
    novo->prox = lista;
    return novo;
  }
  
  if (!p) {
    pR->prox = novo;
  } else { 
    pR->prox = novo;
    novo->prox = p;
  }

  return lista;  
}

void exibirLista2(Celula *lista2) {
  Celula *p;
  for (p = lista2; p; p = p->prox) {
    cout << p->dado << endl;
  }
}


Celula *inserirLista2(int valor1, Celula *lista2) {
  
  Celula *novo = (Celula*)malloc(sizeof(Celula));

  
  novo->dado = valor1;
  novo->prox = NULL;
  Celula *p, *pR;

  if (!lista2) return novo;

  for (pR = NULL, p = lista2; p; pR = p, p = p->prox) {
    if (valor1 == p->dado) {
      
      if (p == lista2) {
        lista2 = lista2->prox;
      } else if (!p->prox) { 
        pR->prox = NULL;
      } else { 
        pR->prox = p->prox;
      }
      free(p);
      return lista2;
    }
  }
  for (pR = NULL, p = lista2; p; pR = p, p = p->prox) {
    if (valor1 < p->dado) break;
  }

  if (p == lista2) {
    novo->prox = lista2;
    return novo;
  }
  
  if (!p) {
    pR->prox = novo;
  } else { 
    pR->prox = novo;
    novo->prox = p;
  }
  
  return lista2;  
}

Celula *excluirLista(int valor, Celula *lista) {
  Celula *p, *pR;

  if (!lista) {
    cout << "Lista vazia. Operação cancelada!" << endl;
    return lista;
  }

  for (pR = NULL, p = lista; p; pR = p, p = p->prox) {
    if (valor == p->dado) {
      
      if (p == lista) {
        lista = lista->prox;
      } else if (!p->prox) { 
        pR->prox = NULL;
      } else {
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

  if (!lista) {
    cout << "Lista vazia. Operação cancelada!" << endl;
    return lista;
  }

  bool houveExclusao;
  do {
    houveExclusao = false;
    for (pR = NULL, p = lista; p; pR = p, p = p->prox) {
      if (valor == p->dado) {
        
        if (p == lista) {
          lista = lista->prox;
        } else if (!p->prox) { 
          pR->prox = NULL;
        } else { 
          pR->prox = p->prox;
        }
        free(p);
        houveExclusao = true;
        break;
      }
    }   
  } while (houveExclusao);
  int contador = 0;
  for (p = lista; p ; p = p->prox) {
    contador++;
  }
  cout<< "quantos numeros foram excluidos" << endl;
  cout<< 30 - contador << endl;
  
  return lista;
}

int contarElementos(Celula *lista) {
  int contador = 0;
  Celula *p;
  for (p = lista; p ; p = p->prox) {
    contador++;
  }
  return contador;
}

float media(Celula *lista) {
  int soma = 0;

  Celula *p;
  for (p = lista; p ; p = p->prox) {
    soma+= p->dado;
  }
  return soma/contarElementos(lista);
}

float mediana(Celula *lista) {
  int quantidadeElementos = contarElementos(lista);
  bool ehPar;

  if (quantidadeElementos % 2 == 0) {
    ehPar = true;
  } else {
    ehPar = false;
  }

  int i;
  int metade;
  Celula *p;
  if (!ehPar) {
    metade = (int)quantidadeElementos/2;
  } else {
    metade = (int)quantidadeElementos/2 - 1;
  }
  for (i = 0, p = lista; i < metade; i++, p = p->prox);

  
  if (!ehPar) return p->dado;
  
  return (p->dado + p->prox->dado)/2;
}

void juntaListas (Celula *lista, Celula *lista2)
{
Celula *p;
Celula *q;
p = lista;
q = lista2;
if(!lista){
  cout<< "lista 1 vazia" << endl;
}else if (!lista2){
  cout<< "lista 2 vazia" << endl;
}else{
  while (p->prox != NULL)
  {
  p = p-> prox;
  }
  p->prox = q;
  } 
};