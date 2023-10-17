package com.example.CRUD.controller;

import com.example.CRUD.model.Pessoa;
import com.example.CRUD.repository.PessoaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
@RequestMapping(path = "/pessoa")

public class PessoaController {
    @Autowired
    private PessoaRepository pessoaRepositorio;

    @GetMapping ("/cadastrar")
    public String cadastrarPessoa(Model model){
        model.addAttribute("pessoa",new Pessoa());
        return"cadastrarPessoa";
    }

    @PostMapping ("/save")
    public String salvarPessoa (@ModelAttribute Pessoa pessoa, Model model){
        pessoaRepositorio .save(pessoa);
        //Cria uma lista atualizada das pessoas cadastradas
        List<Pessoa> listaPessoa = (List<Pessoa>) pessoaRepositorio .findAll();
        model.addAttribute( "pessoas" , listaPessoa );
        return "listarPessoas" ;
    }

    @GetMapping("/listar")
    public String listaProdutos(@ModelAttribute Pessoa pessoa, Model model){
        List<Pessoa> listaPessoa = (List<Pessoa>) pessoaRepositorio.findAll();
        model.addAttribute("pessoas",listaPessoa);
        return "listarPessoas";
    }


}
