
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Perception {

    public ArrayList<Ponto> amostras = new ArrayList();
    public ArrayList<Integer> saidas = new ArrayList();
    public double taxa_aprendizado;
    public int geracoes;
    public int limiar;
    public int numeroAmostras;
    public int numeroAtributos;
    public double[] pesos;

    public Perception(List<Ponto> amostras, List<Integer> saidas, double taxa_aprendizado,
            int geracoes, int limiar) {
        this.amostras = (ArrayList<Ponto>) amostras;
        this.saidas = (ArrayList<Integer>) saidas;
        this.taxa_aprendizado = taxa_aprendizado;
        this.geracoes = geracoes;
        this.limiar = limiar;
        this.numeroAmostras = amostras.size();
        this.pesos = new double[3]; //tamanho deste vetor peso vai ser igual a quantidade de atributos + um valor par limiar
    }

    private int funcao_ativacao_signal(double soma) {
        if (soma >= 0) {
            return 1;
        }
        return -1;
    }

    public void treinar() {
        for (int i = 0; i < this.amostras.size(); i++) {
            amostras.get(i).limiar = this.limiar;
        }

        // Gerar valores randômciso entre 0 e 1 (pesos) conforme o número de atributos
        // A lista de pesos tem tamanho = a quantidade de atributos de uma mostra
        // pesos = [1.0, 0.4, 0.6], por exemplo
        Random gerador = new Random();
        pesos[0] = limiar;
        pesos[1] = gerador.nextDouble();
        pesos[2] = gerador.nextDouble();

        int conta = 0;
        boolean aprendeu;
        double soma;
        int saida_gerada;

        while (true) {
            aprendeu = true;

            // Para cada amostra ou registrou ou ponto ...
            soma = 0;
            for (int i = 0; i < amostras.size(); i++) {
                // Inicializar potencial de ativação
                soma = soma + (amostras.get(i).limiar * pesos[0])
                        + (amostras.get(i).x * pesos[1]) + (amostras.get(i).y * pesos[2]);

                // Obter a saída da rede considerando a função sinal
                saida_gerada = funcao_ativacao_signal(soma);

                // Verificar se a saída da rede é diferente da saída desejada
                // Se sim, calibrar ou treinar ou ajustar ou fazer aprender
                if (saida_gerada != this.saidas.get(i)) {
                    aprendeu = false;
                    double erro = this.saidas.get(i) - saida_gerada;
                    // Fazer o ajuste dos pesos para cada elemento da amostra ou seja, UMA CALIBRAGEM DOS PESOS
                    this.pesos[0] = this.pesos[0] + this.taxa_aprendizado * erro * this.amostras.get(i).limiar;
                    this.pesos[1] = this.pesos[1] + this.taxa_aprendizado * erro * this.amostras.get(i).x;
                    this.pesos[2] = this.pesos[2] + this.taxa_aprendizado * erro * this.amostras.get(i).y;
                }
            }
            // Atualizar contador de gerações
            conta++;

            if (aprendeu || conta > this.geracoes) {
                System.out.println("Gerações de treinamento: " + conta);
                break;
            }
        }
    }

    public void testar(Ponto amostra) {

        amostra.limiar = this.limiar;

        double soma = 0;

        soma = soma + (amostra.limiar * pesos[0]) + (amostra.x * pesos[1]) + (amostra.y * pesos[2]);

        double saida_gerada = this.funcao_ativacao_signal(soma);

        if (saida_gerada == 1) {
            System.out.println("Classe:" + saida_gerada + " ou Time Azul");
        } else {
            System.out.println("Classe:" + saida_gerada + " ou Time Vermelho");
        }

    }

}
