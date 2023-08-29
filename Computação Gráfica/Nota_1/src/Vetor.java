import javax.swing.JOptionPane;

public class Vetor {
	
	private float tamanho;
		
	float vetor[] = new float[3];
	float vetor1[] = new float[3];
					
	public void tamanhovetor() {
	
		vetor[0] = Float.parseFloat(JOptionPane.showInputDialog("valor x"));
		vetor[1] = Float.parseFloat(JOptionPane.showInputDialog("valor y"));
		vetor[2] =Float.parseFloat(JOptionPane.showInputDialog("valor z"));		
		
		String msg;
				
		tamanho = (float) Math.sqrt((vetor[0] * vetor[0]) + (vetor[1] *vetor[1]) +(vetor[2] * vetor[2])  );
		
		msg = "O tamanho do vetor  <"+vetor[0]+" , " + vetor[1] +" , " + vetor[2] +"> é "+ tamanho;
		
		JOptionPane.showMessageDialog(null, msg);
	}
	
	public void normalizar() {
		
		float normalizarx = (vetor[0]/tamanho);		
		float normalizary = (vetor[1]/tamanho);
		float normalizarz = (vetor[2]/tamanho);
		
		String normaliza = "o vetor nomalizador é <" + normalizarx + " , " + normalizary + " , " + normalizarz + ">";
		
		JOptionPane.showMessageDialog(null, normaliza);
	}
	
	public void adicior() {
		if (vetor[0] == 0 && vetor[1] == 0 && vetor[2] == 0 ) {

			vetor[0] = Float.parseFloat(JOptionPane.showInputDialog("valor x"));
			vetor[1] = Float.parseFloat(JOptionPane.showInputDialog("valor y"));
			vetor[2] =Float.parseFloat(JOptionPane.showInputDialog("valor z"));
			
			vetor1[0] = Float.parseFloat(JOptionPane.showInputDialog("valor x"));
			vetor1[1] = Float.parseFloat(JOptionPane.showInputDialog("valor y"));
			vetor1[2] =Float.parseFloat(JOptionPane.showInputDialog("valor z"));
			
			
			float somax = vetor[0] + vetor1[0];
			float somay = vetor[1] + vetor1[1];
			float somaz = vetor[2] + vetor1[2];
			
			String adicao = "soma dos vetores é < " + somax + " , " + somay + " , " + somaz+ ">";
			JOptionPane.showMessageDialog(null, adicao);
			
		} else {						
			
			vetor1[0] = Float.parseFloat(JOptionPane.showInputDialog("valor x"));
			vetor1[1] = Float.parseFloat(JOptionPane.showInputDialog("valor y"));
			vetor1[2] =Float.parseFloat(JOptionPane.showInputDialog("valor z"));
			
			float somax = vetor[0] + vetor1[0];
			float somay = vetor[1] + vetor1[1];
			float somaz = vetor[2] + vetor1[2];
			
			String adicao = "soma dos vetores é < " + somax + " , " + somay + " , " + somaz+ ">";
			JOptionPane.showMessageDialog(null, adicao);
		}
	}
	public void Subtracao() {
		if (vetor[0] == 0 && vetor[1] == 0 && vetor[2] == 0 ) {

			vetor[0] = Float.parseFloat(JOptionPane.showInputDialog("valor x"));
			vetor[1] = Float.parseFloat(JOptionPane.showInputDialog("valor y"));
			vetor[2] =Float.parseFloat(JOptionPane.showInputDialog("valor z"));
			
			vetor1[0] = Float.parseFloat(JOptionPane.showInputDialog("valor x"));
			vetor1[1] = Float.parseFloat(JOptionPane.showInputDialog("valor y"));
			vetor1[2] = Float.parseFloat(JOptionPane.showInputDialog("valor z"));
				
			float subx = vetor[0] - vetor1[0];
			float suby = vetor[1] - vetor1[1];
			float subz = vetor[2] - vetor1[2];
			
			String sub = "subtração dos vetores é  < " + subx + " , " + suby + " , " + subz+ ">";
			JOptionPane.showMessageDialog(null, sub);
			
		} else {
						
			vetor1[0] = Float.parseFloat(JOptionPane.showInputDialog("valor x"));
			vetor1[1] = Float.parseFloat(JOptionPane.showInputDialog("valor y"));
			vetor1[2] = Float.parseFloat(JOptionPane.showInputDialog("valor z"));
	
			float subx = vetor[0] - vetor1[0];
			float suby = vetor[1] - vetor1[1];
			float subz = vetor[2] - vetor1[2];
			
			String sub = "subtração dos vetores é < " + subx + " , " + suby + " , " + subz+ ">";
			JOptionPane.showMessageDialog(null, sub);
		}
	}
	
	public void multiplicacao() {
		if (vetor[0] == 0 && vetor[1] == 0 && vetor[2] == 0) {

			vetor[0] = Float.parseFloat(JOptionPane.showInputDialog("valor x"));
			vetor[1] = Float.parseFloat(JOptionPane.showInputDialog("valor y"));
			vetor[2] =Float.parseFloat(JOptionPane.showInputDialog("valor z"));
			
			float scale = Float.parseFloat(JOptionPane.showInputDialog("valor multiplicação"));	
			
			float scalex = vetor[0] * scale;
			float scaley = vetor[1] * scale;
			float scalez = vetor[2] * scale;
			
			String mult = "multiplicação  é < " + scalex + " , " + scaley + " , " + scalez+ ">";
			JOptionPane.showMessageDialog(null, mult);
			
		} else {
			
			float scale = Float.parseFloat(JOptionPane.showInputDialog("valor da multiplicação"));	
			
			float scalex = vetor[0] * scale;
			float scaley = vetor[1] * scale;
			float scalez = vetor[2] * scale;
			
			String mult = "multiplicação é < " + scalex + " , " + scaley + " , " + scalez+ ">";
			JOptionPane.showMessageDialog(null, mult);
		}
	}
	public void divisao() {
		if (vetor[0] == 0 && vetor[1] == 0 && vetor[2] == 0) {

			vetor[0] = Float.parseFloat(JOptionPane.showInputDialog("valor x"));
			vetor[1] = Float.parseFloat(JOptionPane.showInputDialog("valor y"));
			vetor[2] =Float.parseFloat(JOptionPane.showInputDialog("valor z"));
			
			float scale = Float.parseFloat(JOptionPane.showInputDialog("valor da divisão"));	
			
			float scalex = vetor[0] / scale;
			float scaley = vetor[1] / scale;
			float scalez = vetor[2] / scale;
			
			String div = "a divisão é < " + scalex + " , " + scaley + " , " + scalez+ ">";
			JOptionPane.showMessageDialog(null, div);
			
		} else {
			
			float scale = Float.parseFloat(JOptionPane.showInputDialog("valor multiplicação"));	
			
			float scalex = vetor[0] / scale;
			float scaley = vetor[1] / scale;
			float scalez = vetor[2] / scale;
			
			String div = "a divisão é < " + scalex + " , " + scaley + " , " + scalez+ ">";
			JOptionPane.showMessageDialog(null, div);
		}
	}
	public void produto() {
		if (vetor[0] == 0 && vetor[1] == 0 && vetor[2] == 0) {

			vetor[0] = Float.parseFloat(JOptionPane.showInputDialog("valor x"));
			vetor[1] = Float.parseFloat(JOptionPane.showInputDialog("valor y"));
			vetor[2] =Float.parseFloat(JOptionPane.showInputDialog("valor z"));
			
			vetor1[0] = Float.parseFloat(JOptionPane.showInputDialog("valor x"));
			vetor1[1] = Float.parseFloat(JOptionPane.showInputDialog("valor y"));
			vetor1[2] =Float.parseFloat(JOptionPane.showInputDialog("valor z"));	
			
			float produto = (vetor[0] * vetor1[0])+(vetor[1] * vetor1[1])+(vetor[2] * vetor1[2]);

			String div = "o produto é  " + produto;
			JOptionPane.showMessageDialog(null, div);
			
		} else {
			
			vetor1[0] = Float.parseFloat(JOptionPane.showInputDialog("valor x"));
			vetor1[1] = Float.parseFloat(JOptionPane.showInputDialog("valor y"));
			vetor1[2] =Float.parseFloat(JOptionPane.showInputDialog("valor z"));	
			
			float produto = (vetor[0] * vetor1[0])+(vetor[1] * vetor1[1])+(vetor[2] * vetor1[2]);

			String div = "o produto é  " + produto;
			JOptionPane.showMessageDialog(null, div);
		}
	}
}
