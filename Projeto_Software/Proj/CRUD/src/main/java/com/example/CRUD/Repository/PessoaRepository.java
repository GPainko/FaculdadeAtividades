package com.example.CRUD.Repository;

import com.example.CRUD.Model.Pessoa;
import org.springframework.data.repository.CrudRepository;

// CRUD - Create, Read, Update, Delete da classe Pessoa
public interface PessoaRepository extends CrudRepository <Pessoa, Integer> {

}
