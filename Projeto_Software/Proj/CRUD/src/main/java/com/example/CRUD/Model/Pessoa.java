package com.example.CRUD.Model;

import jakarta.persistence.*;
import java.util.Date;

@Entity
public class Pessoa {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer id;

    @Column(nullable = false)
    private String nome;

    @Column(nullable = false, unique = true)
    private String cpf;

    @Column(nullable = false)
    private String senha;

    @Transient
    private String confirmarSenha;

    @Column(nullable = false)
    private Integer kv;

    @Column(nullable = false)
    private Integer ms;

    @Column(nullable = false)
    private Integer ma;

    @Column(nullable = false)
    private Float espessura;

    @Column(nullable = false)
    private String resultado;

    @Temporal(TemporalType.TIMESTAMP)
    @Column(nullable = false)
    private Date dataCalculo;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public String getConfirmarSenha() {
        return confirmarSenha;
    }

    public void setConfirmarSenha(String confirmarSenha) {
        this.confirmarSenha = confirmarSenha;
    }

    public Integer getKv() {
        return kv;
    }

    public void setKv(Integer kv) {
        this.kv = kv;
    }

    public Integer getMs() {
        return ms;
    }

    public void setMs(Integer ms) {
        this.ms = ms;
    }

    public Integer getMa() {
        return ma;
    }

    public void setMa(Integer ma) {
        this.ma = ma;
    }

    public Float getEspessura() {
        return espessura;
    }

    public void setEspessura(Float espessura) {
        this.espessura = espessura;
    }

    public String getResultado() {
        return resultado;
    }

    public void setResultado(String resultado) {
        this.resultado = resultado;
    }

    public Date getDataCalculo() {
        return dataCalculo;
    }

    public void setDataCalculo(Date dataCalculo) {
        this.dataCalculo = dataCalculo;
    }
}
