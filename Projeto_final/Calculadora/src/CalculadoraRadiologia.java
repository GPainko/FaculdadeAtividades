import java.util.Scanner;

public class CalculadoraRadiologia {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Por favor, entre com o valor de mGy: ");
            double mGy = scanner.nextDouble();

            System.out.print("Por favor, entre com o valor de MAs: ");
            double mAs = scanner.nextDouble();

            System.out.print("Por favor, entre com o valor de dfs: ");
            double dfs = scanner.nextDouble();

            System.out.print("Por favor, entre com o valor de BSF: ");
            double bsf = scanner.nextDouble();

            // Calcula o rendimento
            double rendimento = mGy / mAs;

            // Calcula o ESAK
            double esak = rendimento * Math.pow(80 / dfs, 2) * mAs * bsf;

            System.out.println("O rendimento calculado é: " + rendimento + " mGy/MAs");
            System.out.println("O ESAK calculado é: " + esak + " mGY");

        } catch (Exception e) {
            System.out.println("Erro ao calcular. Certifique-se de inserir valores numéricos válidos.");
        } finally {
            scanner.close();
        }
    }
}