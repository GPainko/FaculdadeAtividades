package com.example.CRUD.Model;

public class Calculadora {
    public String esak(){

        DadosHTML dm = new DadosHTML();

        double dfs;
        String regiao = dm.getRegiao();
        int espessura = dm.getEspessura();
        int ma = dm.getMa();
        int rendimento = 1;
        int bsf = 1;


        if (regiao.equals("torax")){
            dfs = 180 - espessura;
        }
        else {
            dfs = 100 - espessura;
        }
        double esak = rendimento * (Math.pow((80/dfs),2)) * ma * bsf;

        return Double.toString(esak);
    }

}
