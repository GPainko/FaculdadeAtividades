
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;


public class Cliente {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        try {
            //Cria um socket e tenta se conectar ao servidor na porta 1234
            Socket s = new Socket("localhost", 1234);

            //cria uma thread para receber mensagens em paralelo a thread principal
            Thread t = new Thread() {
                public void run() {
                    while (true) {
                        try {
                            //aguarda uma mensagem do servidor
                            DataInputStream in = new DataInputStream(s.getInputStream());
                            DataOutputStream out = new DataOutputStream(s.getOutputStream());                    
                            String msgRecebida = in.readUTF(); //bloqueante
                            System.out.println(msgRecebida);
                            String msgresposta = teclado.nextLine();
                            out.writeUTF(msgresposta);
                        } catch (IOException ex) {
                            
                            System.out.println("Erro na thread de recebimento de mensagens");
                        }
                    }
                }
            };
            t.start();
            
            
                //Envia uma mensagem ao servidor
            DataOutputStream out = new DataOutputStream(s.getOutputStream());
            System.out.println("Qual operação deseja realizar:(saque, depósito e consulta do saldo ");
            String msgop = teclado.nextLine();
            out.writeUTF(msgop);

        } catch (IOException ex) {
            System.out.println("Erro - servidor não encontrado");
        }
    }

    private static void print(String digite_o_valor_valor_1) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
