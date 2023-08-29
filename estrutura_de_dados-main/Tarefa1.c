#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct no {
    char dado;
    struct no *prox; //ponteiro para o proximo elemento dessa estrutura
} Celula;

Celula *inserir(char valor, Celula *topo) {
    //alocar memoria
    Celula *novo = (Celula *)malloc(sizeof(Celula));
        
    //depositar valor
    novo->dado = valor;

    //engatar o novo no ultimo
    novo->prox = topo;

    //retornar o novo top
    return novo;
}

Celula *remover(Celula *topo) {
    //testar se pilha vazia
    if (!topo) {
        printf("Pilha vazia. Operacao nao realizada\n");
        return topo;
    }

    //ponteiro lixo apontar para o topo/ultimo
    Celula *lixo = topo;

    //topo avanca 
    topo = topo->prox;

    //liberar lixo
    free(lixo);

    //retornar novo topo
    return topo;
}

int contarNos(Celula *topo) {
    int qtd = 0;
    Celula *p;
    for (p = topo; p ; p = p->prox){
        qtd++;
    }
    return qtd;
}

void exibir(Celula *topo) {
    if (!topo) {
        printf("Pilha vazia\n");
        return;
    }
    Celula *p;
    for (p = topo; p ; p = p->prox){
        printf("%c\t", p->dado);
    } 

}

int main()
{
    char nomeArquivo[200]; 
    FILE *procurador;
    int qtdParticulas;
    int x;

    printf("Nome do arquivo de saida contendo as particulas: ");
    scanf("%s", nomeArquivo);

    procurador = fopen(nomeArquivo, "w");
    printf("Arquivo criado com sucesso!\n");

    printf("Quantas particulas quer gerar? ");
    scanf("%d", &qtdParticulas);

    srand(time(NULL));
    for (; qtdParticulas > 0; qtdParticulas--)
    {
        printf("digite um valor: ");
        scanf("%i",&x);
        
        fprintf(procurador, "%d\n", x); 
        fflush(procurador);
    }

    fclose(procurador);

    char entrada = x+'0';
  
    Celula *pilha1 = NULL;          //pilha1 é um ponteiro de Celula que vai apontar para o ultimo elemento inserido
    pilha1 = inserir(entrada, pilha1);
    pilha1 = inserir(entrada, pilha1);
    pilha1 = inserir(entrada, pilha1);
    pilha1 = inserir(entrada, pilha1);
    pilha1 = inserir(entrada, pilha1);

    printf("Endereco do ultimo elemento: %p\n",pilha1);
    printf("Valor do ultimo elemenbto  : %c\n",pilha1->dado);  

    printf("O tamanho da pilha1 eh: %d\n", contarNos(pilha1));  
    exibir(pilha1);

    return 1;
}