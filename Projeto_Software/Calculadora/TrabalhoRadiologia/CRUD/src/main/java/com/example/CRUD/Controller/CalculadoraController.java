package com.example.CRUD.Controller;

import com.example.CRUD.Model.Calculadora;
import org.springframework.stereotype.Controller;

@Controller
public class CalculadoraController {
    double espessura;
    double bsf;
    double mas;
    double kV;
    double rendimento;

   Calculadora esak= new Calculadora(rendimento,espessura,mas,bsf);

   double resultado = esak.calculaESAK();
}
