import javax.swing.JOptionPane;

public class MenuMatriz {
	public static void matrizes() {
        int op = 0;

        Menu menu = new Menu();
        Matriz matriz = new Matriz();

        while (op != 6) {
            op = menu.getOptionMatriz();
            switch (op) {
                case 1: {
                	matriz.valoresmatriz();               	
                	matriz.somar();
                	matriz.subtrair();
                	break;
                }
                case 2: {
                	matriz.valoresmatriz1();
                	matriz.multiplicar();
                	matriz.dividir();
                    break;
                }
                case 3: {
                	matriz.valoresmatriz1();
                	matriz.valoresvetor();
                	matriz.multiplicarVetor();
                    break;
                }
                case 4: {
                	matriz.valoresmatriz();
                	matriz.multiplicarMatriz();
                    break;
                }
                case 5: {
                	matriz.valoresmatriz1();
                	matriz.valoresmatrizTransposta();
                    break;
                }               
                case 6: {
                    Principal.main(null);
                    break;
                }
                default: {
                    JOptionPane.showMessageDialog(null, "Você digitou uma opção inválida");
                    break;
                }
            }
        }
	}
}
