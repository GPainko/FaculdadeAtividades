import javax.swing.JOptionPane;

public class Menu {
    public int getOption(){
        String menuOpcoes = " MENU DE OPÇÕES :::\n" +
                    "[1] - Vetor \n" +
                    "[2] - Matriz\n"+
                    "[3] - Sair";
     return Integer.parseInt(JOptionPane.showInputDialog(menuOpcoes));
    }
    
    public int getOptionVetor(){
    	String menuOpcoes = "::: Vetor :::\n" +
                "[1] - Tamanho do vetor \n" +
                "[2] - Normalizar o vetor\n"+
                "[3] - Adicionar outro vetor\n"+
                "[4] - Subtrair outro vetor\n"+
                "[5] - Ler o valor de um escalar e realizar a multiplicação\n"+
                "[6] - Ler o valor de um escalar e realizar a divisão\n"+
                "[7] - Calcular o produto escalar do vetor lido anteriormente por outro vetor\n"+
                "[8] - Sair";
     return Integer.parseInt(JOptionPane.showInputDialog(menuOpcoes));
    }
    
    public int getOptionMatriz(){
    	String menuOpcoes = "::: Matriz :::\n" +
                "[1] - Adição e subtração de outra matriz \n" +
                "[2] - Multiplicação e Divisão de um escalar\n"+
                "[3] - Multiplicação da matriz por um vetor de 3 elementos\n"+
                "[4] - Multiplicação da matriz por outra matriz 3x3,\n"+
                "[5] - Apresentar a transposta da matriz lida inicialmente.\n"+                
                "[6] - Sair";
     return Integer.parseInt(JOptionPane.showInputDialog(menuOpcoes));
    }
    
}