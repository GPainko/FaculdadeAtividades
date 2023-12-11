package com.example.CRUD.Model;

public class Calculadora {
    private double rendimento,espessura,mas,bsf;

    private boolean isTorax;

    public Calculadora() {
    }

    public Calculadora(double rendimento, double espessura, double mas, double bsf, boolean isTorax ) {
        this.rendimento = rendimento;
        this.espessura = espessura;
        this.mas = mas;
        this.bsf = bsf;
        this.isTorax = isTorax;
    }

    public double calculaESAK(){
        double dfs;
        if (isTorax){
            dfs = 180 - espessura;
        }
        else {
            dfs = 100 - espessura;
        }
        return rendimento * (Math.pow((80/dfs),2)) * this.mas * this.bsf;
    }

    public double getRendimento() {
        return rendimento;
    }

    public void setRendimento(double rendimento) {
        this.rendimento = rendimento;
    }

    public double getEspessura() {
        return espessura;
    }

    public void setEspessura(double espessura) {
        this.espessura = espessura;
    }

    public double getMas() {
        return mas;
    }

    public void setMas(double mas) {
        this.mas = mas;
    }
    public double getBsf() {
        return bsf;
    }

    public void setBsf(double bsf) {
        this.bsf = bsf;
    }

    public boolean isTorax() {
        return isTorax;
    }

    public void setTorax(boolean torax) {
        isTorax = torax;
    }
}
