
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Principal {

    public static void main(String[] args) {

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
                            String msgRecebida1 = in.readUTF();//bloqueante
                            String msgRecebida2 = in.readUTF();
                            String msgRecebida3 = in.readUTF();
                            int msgRecebida1int1 = Integer.parseInt(msgRecebida1);
                            int msgRecebida1int2 = Integer.parseInt(msgRecebida2);

                            if (msgRecebida3.equals("+")) {
                                int msgSoma = msgRecebida1int1 + msgRecebida1int2;
                                String msgSomaS = String.valueOf(msgSoma);
                                out.writeUTF(msgSomaS);
                            } else if (msgRecebida3.equals("-")) {
                                int msgSoma = msgRecebida1int1 - msgRecebida1int2;
                                String msgSomaS = String.valueOf(msgSoma);
                                out.writeUTF(msgSomaS);
                            } else if (msgRecebida3.equals("*")) {
                                int msgSoma = msgRecebida1int1 * msgRecebida1int2;
                                String msgSomaS = String.valueOf(msgSoma);
                                out.writeUTF(msgSomaS);
                            } else if (msgRecebida3.equals("/")) {
                                int msgSoma = msgRecebida1int1 - msgRecebida1int2;
                                String msgSomaS = String.valueOf(msgSoma);
                                out.writeUTF(msgSomaS);
                            } else {
                                out.writeUTF("operação invalida");
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
