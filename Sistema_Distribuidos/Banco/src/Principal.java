
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class Principal {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        try {
            //cria um servidor e aloca a porta 1234 para ele
            ServerSocket servidor = new ServerSocket(1234);

            //aguarda uma conexão
            Socket cliente = servidor.accept(); //bloqueante
            System.out.println("Recebi uma conexão");

            //cria uma thread para receber mensagens do cliente
            Thread t = new Thread() {
                public void run() {
                    //aguarda uma mensagem do cliente
                    while (true) {
                        try {
                            DataInputStream in = new DataInputStream(cliente.getInputStream());
                            DataOutputStream out = new DataOutputStream(cliente.getOutputStream());
                            while(true){
                                String msgRecebida = in.readUTF();//bloqueante                           
                            int msgRecebidaint = Integer.parseInt(msgRecebida);
                            int saldo = 1000;
                            
                            if (msgRecebidaint == 1) {
                                if (saldo == 0) {
                                    out.writeUTF("saldio insuficiente");
                                } else {
                                    out.writeUTF("quantidade que deseja sacar");
                                    String msgRecebidasaque = in.readUTF();
                                    int quantidadesaque = Integer.parseInt(msgRecebidasaque);
                                    int saque = saldo - quantidadesaque;
                                    String Enviarsaque = String.valueOf(saque);
                                    out.writeUTF(Enviarsaque);                                    
                                }
                            } else if (msgRecebidaint == 2) {
                                out.writeUTF("quantidade que deseja depositar");
                                String msgRecebidadeposito = in.readUTF();
                                int quantidadedeposito = Integer.parseInt(msgRecebidadeposito);
                                int deposito = saldo + quantidadedeposito;
                                String Enviardeposiyo = String.valueOf(deposito);
                                out.writeUTF(Enviardeposiyo);
                            } else if (msgRecebidaint == 3) {
                                String Enviarsaldo = String.valueOf(saldo);
                                out.writeUTF(Enviarsaldo);
                            } else {
                                out.writeUTF("operação invalida");
                            }
                            }

                        } catch (IOException e) {
                            System.out.println("Erro na thread de recebimento de mensagens do servidor");
                        }
                    }
                }
            };
            t.start();
        } catch (IOException ex) {
            System.out.println("Erro - porta já em uso");
        }
    }
}
