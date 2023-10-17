package com.example.CRUD.model;

import jakarta.persistence.*;

@Entity
public class Pessoa {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer id;
    @Column(nullable = false)
    private String  nome;
    @Column(nullable = false, unique = true)
    private String email;
    @Column(length = 15)
    private String fone;

    public Pessoa() {
    }
    public Pessoa(Integer id,String nome,String email, String fone) {
        this.id = id;
        this.nome = nome;
        this.email = email;
        this.fone = fone;
    }
    public Pessoa(String nome,String email, String fone) {
        this.nome = nome;
        this.email = email;
        this.fone = fone;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

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

    public String getFone() {
        return fone;
    }

    public void setFone(String fone) {
        this.fone = fone;
    }
}

