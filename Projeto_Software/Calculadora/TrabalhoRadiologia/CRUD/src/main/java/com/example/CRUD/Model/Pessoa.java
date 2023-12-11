package com.example.CRUD.Model;

import jakarta.persistence.*;

@Entity // Comunica com o JPA para entender essa classe como uma entidade (BD)
public class Pessoa {
    @Id // diz para o JPA que o ID é um indentificador (PK)
    @GeneratedValue(strategy = GenerationType.AUTO)//auto_increment
    private Integer id;
    @Column(nullable = false) //Coluna nao pode ser nula
    private String nome;
    @Column(nullable = false, unique = true)//NOT NULL UNIQUE
    private String email;
    @Column(length = 15)//esta coluna é um varchar 15
    private String fone;

    public Pessoa() {
    }

    public Pessoa(Integer id, String nome, String email, String fone) {
        this.id = id;
        this.nome = nome;
        this.email = email;
        this.fone = fone;
    }

    public Pessoa(String nome, String email, String fone) {
        this.nome = nome;
        this.email = email;
        this.fone = fone;
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

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getFone() {
        return fone;
    }

    public void setFone(String fone) {
        this.fone = fone;
    }
}
