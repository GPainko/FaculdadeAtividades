package com.example.CRUD.Controller;

import com.example.CRUD.Repository.PessoaRepository;
import com.example.CRUD.Model.Pessoa;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;
import org.springframework.ui.Model;

import java.util.List;

@Controller // siguinifica que esta calsse é uma controller
@RequestMapping(path = "/pessoa") //mapping que acessa essa classe
public class PessoaController {
    @Autowired//marcação de atribto que acessa o crud de pessoa
    private PessoaRepository pessoaRepository;
    //redireciona para pagina cadastro

    @GetMapping("/cadastrar")
    public String cadastrarPessoa(Model model) {
        //mandar um obj de tipo pessoa para a pagina cadastro
        model.addAttribute("pessoa", new Pessoa());
        //redirecionar para a pagina cadastrarPessoa.html
        return "cadastrarPessoa";

    }

    @PostMapping ("/save")
    public String salvarPessoa (@ModelAttribute Pessoa pessoa, Model model){
        pessoaRepository .save(pessoa);
        //Cria uma lista atualizada das pessoas cadastradas
        List<Pessoa> listaPessoa = (List<Pessoa>) pessoaRepository .findAll();
        model.addAttribute( "pessoas" , listaPessoa );
        return "listar" ;
    }

    @GetMapping("/listar")
    public String listaProdutos(@ModelAttribute Pessoa pessoa, Model model){
        List<Pessoa> listaPessoa = (List<Pessoa>) pessoaRepository.findAll();
        model.addAttribute("pessoas",listaPessoa);
        return "listar";
    }

    @GetMapping ("/excluir/{id}" )
    public String excluirPessoa (Model model, @PathVariable Long id) {
        pessoaRepository .deleteById( Math.toIntExact(id));
        List<Pessoa> listaPessoa = (List<Pessoa>) pessoaRepository .findAll();
        model.addAttribute( "pessoas", listaPessoa );
        return "listar" ;
    }

    @GetMapping ("/alterar/{id}" )
    public String altPessoa(@PathVariable Long id, Model model) {
        Pessoa p = pessoaRepository .findById(Math.toIntExact(id)).get();
        model.addAttribute( "pessoa", p);
        return "alterar" ;
    }

    @PostMapping ("/alterar")
    public String alterarProduto (@ModelAttribute Pessoa novaPessoa, Model model) {
        pessoaRepository .save(novaPessoa);
        List<Pessoa> listaPessoa = (List<Pessoa>) pessoaRepository .findAll();
        model.addAttribute( "pessoas", listaPessoa );
        return "listar" ;
    }

}

