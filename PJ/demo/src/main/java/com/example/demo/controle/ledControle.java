package com.example.demo.controle;

import com.example.demo.model.Arduino;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping(path = "/led")
public class ledControle {

    Arduino ad = new Arduino();
    @GetMapping("/ligar")
    public String ligar(){
        ad.comunicacaoArduino(1);
        return "Ligado";
    }

    @GetMapping("/desligar")
    public String Desligar(){
        ad.comunicacaoArduino(2);
        return "desligar";
    }

}
