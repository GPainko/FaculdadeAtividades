
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Program {

    public static void main(String[] args) {
        System.out.println("Exemplo de RNA Perceptron para classificação de equipes");
        ArrayList<Ponto> amostras = new ArrayList();

        amostras.add(new Ponto(0.72, 0.82));
        amostras.add(new Ponto(0.91, -0.69));
        amostras.add(new Ponto(0.46, 0.80));
        amostras.add(new Ponto(0.03, 0.93));
        amostras.add(new Ponto(0.12, 0.25));
        amostras.add(new Ponto(0.96, 0.47));
        amostras.add(new Ponto(0.8, -0.75));
        amostras.add(new Ponto(0.46, 0.98));
        amostras.add(new Ponto(0.66, 0.24));
        amostras.add(new Ponto(0.72, -0.15));
        amostras.add(new Ponto(0.35, 0.01));
        amostras.add(new Ponto(-0.16, 0.84));
        amostras.add(new Ponto(-0.04, 0.68));
        amostras.add(new Ponto(-0.11, 0.1));
        amostras.add(new Ponto(0.31, -0.96));
        amostras.add(new Ponto(0.0, -0.26));
        amostras.add(new Ponto(-0.43, -0.65));
        amostras.add(new Ponto(0.57, -0.97));
        amostras.add(new Ponto(-0.47, -0.03));
        amostras.add(new Ponto(-0.72, -0.64));
        amostras.add(new Ponto(-0.57, 0.15));
        amostras.add(new Ponto(-0.25, -0.43));
        amostras.add(new Ponto(0.47, -0.88));
        amostras.add(new Ponto(-0.12, -0.9));
        amostras.add(new Ponto(-0.58, 0.62));
        amostras.add(new Ponto(-0.48, 0.05));
        amostras.add(new Ponto(-0.79, -0.92));
        amostras.add(new Ponto(-0.42, -0.09));
        amostras.add(new Ponto(-0.76, 0.65));
        amostras.add(new Ponto(-0.77, -0.76));

        ArrayList<Integer> saidas = new ArrayList<>();
        
        Collections.addAll(saidas, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 
                -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
        
        double taxa_aprendizado = 0.1;
        int geracoes = 1000;
        int limiar = 1;
        Perception p = new Perception(amostras, saidas, taxa_aprendizado, geracoes, limiar);

        p.treinar();

        String op;
        do {
            //Console.Write("\n ");
            //double x = Double.Parse(Console.ReadLine());
            System.out.println("\n Informe valor para x(-1 a 1):");
            Scanner in = new Scanner(System.in);
            double x;
            x = Double.parseDouble(in.nextLine());

            double y;
            System.out.println("\n nforme valor para y(-1 a 1):");
            Scanner in1 = new Scanner(System.in);
            y = Double.parseDouble(in1.nextLine());

            p.testar(new Ponto(x, y));
            //Console.Write("1 - Sair: ");
            System.out.println("1-sair");
            Scanner in12 = new Scanner(System.in);
            String r = in12.nextLine();
            op = r;
        } while (!"1".equals(op));

    }
}
