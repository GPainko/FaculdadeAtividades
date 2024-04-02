#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char** argv) {
    int rank, size;
    int n = 6; // tamanho dos vetores
    double *vetor1, *vetor2, *resultado, *vetor_local1, *vetor_local2, *resultado_local;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Inicializa os vetores
    if (rank == 0) {
        vetor1 = (double*)malloc(n * sizeof(double));
        vetor2 = (double*)malloc(n * sizeof(double));
        resultado = (double*)malloc(n * sizeof(double));
        for (int i = 0; i < n; i++) {
            vetor1[i] = i + 1;
            vetor2[i] = 2 * (i + 1);
        }
    }

    // Distribui partes dos vetores para cada processo
    int elements_per_process = n / size;
    vetor_local1 = (double*)malloc(elements_per_process * sizeof(double));
    vetor_local2 = (double*)malloc(elements_per_process * sizeof(double));
    resultado_local = (double*)malloc(elements_per_process * sizeof(double));
    MPI_Scatter(vetor1, elements_per_process, MPI_DOUBLE, vetor_local1, elements_per_process, MPI_DOUBLE, 0, MPI_COMM_WORLD);
    MPI_Scatter(vetor2, elements_per_process, MPI_DOUBLE, vetor_local2, elements_per_process, MPI_DOUBLE, 0, MPI_COMM_WORLD);

    // Calcula a soma localmente
    for (int i = 0; i < elements_per_process; i++) {
        resultado_local[i] = vetor_local1[i] + vetor_local2[i];
    }

    // Reúne os resultados parciais
    MPI_Gather(resultado_local, elements_per_process, MPI_DOUBLE, resultado, elements_per_process, MPI_DOUBLE, 0, MPI_COMM_WORLD);

    // Imprime o resultado no processo 0
    if (rank == 0) {
        printf("Vetor resultado:\n");
        for (int i = 0; i < n; i++) {
            printf("%f ", resultado[i]);
        }
        printf("\n");
    }

    MPI_Finalize();
    return 0;
}

