package com.example.demo.model;
import com.example.demo.controle.ledControle;

import javax.swing.JButton;

/**
 * @author klauder
 */
public class Arduino {
    private ControlePorta arduino;

    /**
     * Construtor da classe Arduino
     */
    public Arduino() {
        arduino = new ControlePorta("COM3", 9600);//Windows - porta e taxa de transmissão
        //arduino = new ControlePorta("/dev/ttyUSB0",9600);//Linux - porta e taxa de transmissão
    }

    public void comunicacaoArduino(int opcao) {
        arduino.enviaDados(opcao);
    }
}