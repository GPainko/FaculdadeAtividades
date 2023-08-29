import javax.swing.JOptionPane;

public class Principal {
	public static void main(String[] args) {
        int op = 0;

        Menu menu = new Menu();
        
        
        while (op != 6) {
            op = menu.getOption();
            switch (op) {
                case 1: {                	
                	MenuVetor.vetores();
                    break;
                }
                case 2: {
                	MenuMatriz.matrizes();
                    break;
                }
                case 3: {
                    System.exit(0);
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
