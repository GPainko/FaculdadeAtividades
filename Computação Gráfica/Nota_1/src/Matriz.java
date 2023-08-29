
import javax.swing.JOptionPane;

public class Matriz {
	
	float matriz[][] = new float[3][3];
	float matriz1[][] = new float[3][3];
	float matriz2[][] = new float[3][3];
	float matriz3[][] = new float[3][1];
	float vetor[] = new float[3];
	int i;
	int linha;
	int coluna;
	float escalar;
	
	public void valoresmatriz() {
		System.out.println("primeira matriz");		
		for (linha = 0;linha < matriz.length;linha++) {
			for (coluna = 0;coluna < matriz[linha].length;coluna++) {
						matriz[linha][coluna] = Float.parseFloat(JOptionPane.showInputDialog("valores primeira matriz"));
			}	
		}
		for (linha = 0;linha < matriz.length;linha++) {
			for (coluna = 0;coluna < matriz[linha].length;coluna++) {
					System.out.print(matriz[linha][coluna] + " - ");
			}
			System.out.println(" ");
		}
		
		System.out.println("segunda matriz");	
		for (linha = 0;linha < matriz1.length;linha++) {
			for (coluna = 0;coluna < matriz1[linha].length;coluna++) {
						matriz1[linha][coluna] = Float.parseFloat(JOptionPane.showInputDialog("valores segunda matriz"));
			}	
		}
		for (linha = 0;linha < matriz1.length;linha++) {
			for (coluna = 0;coluna < matriz1[linha].length;coluna++) {
					System.out.print(matriz1[linha][coluna] + " - ");
			}
			System.out.println(" ");
		}
				
	}
	
	public void valoresmatriz1() {
		System.out.println("primeira matriz");	
		for (linha = 0;linha < matriz.length;linha++) {
			for (coluna = 0;coluna < matriz[linha].length;coluna++) {
						matriz[linha][coluna] = Float.parseFloat(JOptionPane.showInputDialog("valores da matriz"));
			}	
		}
		for (linha = 0;linha < matriz.length;linha++) {
			for (coluna = 0;coluna < matriz[linha].length;coluna++) {
					System.out.print(matriz[linha][coluna] + " - ");
			}
			System.out.println(" ");
		}
				
	}
	
	public void valoresvetor() {
		System.out.println("valores vetor");
		for(i = 0;i <vetor.length; i++) {
			vetor[i] = Float.parseFloat(JOptionPane.showInputDialog("valores do vetor"));
		}
		for(i = 0;i <vetor.length; i++) {
			System.out.println(vetor[i]);
		}
	}
	
	public void somar() {
				
		System.out.println(" soma das matrizes ");
		
		for (linha = 0;linha < matriz2.length;linha++) {
			for (coluna = 0;coluna < matriz2[linha].length;coluna++) {
						matriz2[linha][coluna]= matriz[linha][coluna] + matriz1[linha][coluna];
			}	
		}
		for (linha = 0;linha < matriz2.length;linha++) {
			for (coluna = 0;coluna < matriz2[linha].length;coluna++) {
					System.out.print(matriz2[linha][coluna] + " - ");
			}
			System.out.println(" ");
		}				 		
	}
	public void subtrair() {
		
		System.out.println(" subtração das matrizes ");
		
		for (linha = 0;linha < matriz2.length;linha++) {
			for (coluna = 0;coluna < matriz2[linha].length;coluna++) {
						matriz2[linha][coluna]= matriz1[linha][coluna] - matriz[linha][coluna];
			}	
		}
		for (linha = 0;linha < matriz2.length;linha++) {
			for (coluna = 0;coluna < matriz2[linha].length;coluna++) {
					System.out.print(matriz2[linha][coluna] + " - ");
			}
			System.out.println(" ");
		}				 		
	}
	
	public void multiplicar() {
		System.out.println(" multiplipação escalar da matriz");
		escalar = Float.parseFloat(JOptionPane.showInputDialog("valor da multiplicação"));
		for (linha = 0;linha < matriz1.length;linha++) {
			for (coluna = 0;coluna < matriz[linha].length;coluna++) {
						matriz1[linha][coluna]= matriz[linha][coluna] * escalar;;
			}	
		}
		for (linha = 0;linha < matriz1.length;linha++) {
			for (coluna = 0;coluna < matriz1[linha].length;coluna++) {
					System.out.print(matriz1[linha][coluna] + " - ");
			}
			System.out.println(" ");
		}				 		
	}
	
	public void dividir() {
		System.out.println(" divisão da matriz");
		escalar = Float.parseFloat(JOptionPane.showInputDialog("valor da divisão"));
		for (linha = 0;linha < matriz.length;linha++) {
			for (coluna = 0;coluna < matriz[linha].length;coluna++) {
						matriz2[linha][coluna]= matriz[linha][coluna] / escalar;;
			}	
		}
		for (linha = 0;linha < matriz2.length;linha++) {
			for (coluna = 0;coluna < matriz2[linha].length;coluna++) {
					System.out.print(matriz2[linha][coluna] + " - ");
			}
			System.out.println(" ");
		}				 		
	}
	
	public void multiplicarVetor() {		
		matriz3[0][0] = matriz[0][0] * vetor[0] + matriz [0][1] * vetor[1] + matriz [0][2] * vetor[2];
		matriz3[1][0] = matriz[1][0] * vetor[0] + matriz [1][1] * vetor[1] + matriz [1][2] * vetor[2];
		matriz3[2][0] = matriz[2][0] * vetor[0] + matriz [2][1] * vetor[1] + matriz [2][2] * vetor[2];
		
		System.out.println(" multiplicação pelo vetor");
		
		for (linha = 0;linha < matriz3.length;linha++) {
			for (coluna = 0;coluna < matriz3[linha].length;coluna++) {
					System.out.print(matriz3[linha][coluna]);
			}
			System.out.println(" ");
		}				 		
	}
	
	public void multiplicarMatriz() {		
		
		matriz2[0][0] = matriz[0][0] * matriz1[0][0] + matriz[0][1] * matriz1[1][0] + matriz[0][2] * matriz1[2][0];
		matriz2[1][0] = matriz[1][0] * matriz1[0][0] + matriz[1][1] * matriz1[1][0] + matriz[1][2] * matriz1[2][0];
		matriz2[2][0] = matriz[2][0] * matriz1[0][0] + matriz[2][1] * matriz1[1][0] + matriz[2][2] * matriz1[2][0];
		
		matriz2[0][1] = matriz[0][0] * matriz1[0][1] + matriz[0][1] * matriz1[1][1] + matriz[0][2] * matriz1[2][1];
		matriz2[1][1] = matriz[1][0] * matriz1[0][1] + matriz[1][1] * matriz1[1][1] + matriz[1][2] * matriz1[2][1];
		matriz2[2][1] = matriz[2][0] * matriz1[0][1] + matriz[2][1] * matriz1[1][1] + matriz[2][2] * matriz1[2][1];
		
		matriz2[0][2] = matriz[0][0] * matriz1[0][2] + matriz[0][1] * matriz1[1][2] + matriz[0][2] * matriz1[2][2];
		matriz2[1][2] = matriz[1][0] * matriz1[0][2] + matriz[1][1] * matriz1[1][2] + matriz[1][2] * matriz1[2][2];
		matriz2[2][2] = matriz[2][0] * matriz1[0][2] + matriz[2][1] * matriz1[1][2] + matriz[2][2] * matriz1[2][2];
		
		System.out.println(" multiplicação de matrix 3x3");
		
		for (linha = 0;linha < matriz2.length;linha++) {
			for (coluna = 0;coluna < matriz2[linha].length;coluna++) {
					System.out.print(matriz2[linha][coluna] + " - ");
			}
			System.out.println(" ");
		}				 		
	}
	
	public void valoresmatrizTransposta() {
		System.out.println("primeira matriz transposta");			
		for (linha = 0;linha < matriz.length;linha++) {
			for (coluna = 0;coluna < matriz[linha].length;coluna++) {
					System.out.print(matriz[coluna][linha] + " - ");
			}
			System.out.println(" ");
		}
				
	}
	
}
