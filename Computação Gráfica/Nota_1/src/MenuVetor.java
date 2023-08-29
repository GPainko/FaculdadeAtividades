import javax.swing.JOptionPane;

public class MenuVetor {
	public static void vetores() {
        int op = 0;

        Menu menu = new Menu();
        Vetor vetor = new Vetor();

        while (op != 6) {
            op = menu.getOptionVetor();
            switch (op) {
                case 1: {
                	vetor.tamanhovetor();
                	break;
                }
                case 2: {
                	vetor.normalizar();
                    break;
                }
                case 3: {
                	vetor.adicior();
                    break;
                }
                case 4: {
                	vetor.Subtracao();
                    break;
                }
                case 5: {
                	vetor.multiplicacao();
                    break;
                }
                case 6: {
                	vetor.divisao();
                    break;
                }
                case 7: {
                	vetor.produto();
                    break;
                }
                case 8: {
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
