import java.util.Scanner;

public class ESAKCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicitando os parâmetros do usuário
        System.out.println("Insira o Rendimento (mGy/Mas): ");
        double rendimento = scanner.nextDouble();

        System.out.println("Insira o valor de dfs: ");
        double dfs = scanner.nextDouble();

        System.out.println("Insira o valor do mAs: ");
        double mAs = scanner.nextDouble();

        System.out.println("Insira o fator de retroespalhamento (BSF): ");
        double BSF = scanner.nextDouble();

        // Calculando o ESAK (mGY)
        double ESAK = calculateESAK(rendimento, dfs, mAs, BSF);

        // Exibindo o resultado
        System.out.printf("O ESAK (mGY) calculado é: %.2f\n", ESAK);

        scanner.close();
    }

    public static double calculateESAK(double rendimento, double dfs, double mAs, double BSF) {
        // Implementação da fórmula fornecida
        return rendimento * Math.pow((80 / dfs), 2) * mAs * BSF;
    }
}