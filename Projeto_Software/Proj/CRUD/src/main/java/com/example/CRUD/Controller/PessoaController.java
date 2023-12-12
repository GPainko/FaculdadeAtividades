package com.example.CRUD.Controller;

import com.example.CRUD.Model.Pessoa;
import com.example.CRUD.Model.PessoaDTO;
import com.example.CRUD.Repository.PessoaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class PessoaController {

    @Autowired
    private PessoaRepository pessoaRepository;

    @GetMapping("/cadastrar")
    public String mostrarFormulario(Model model) {
        model.addAttribute("pessoaDTO", new PessoaDTO());
        return "cadastrar";
    }

    @PostMapping("/pessoa/save")
    public String salvarPessoa(@ModelAttribute("pessoaDTO") PessoaDTO pessoaDTO, BindingResult result) {
        if (result.hasErrors()) {
            return "cadastrar";
        }

        Pessoa pessoa = convertPessoaDTOToPessoa(pessoaDTO);
        pessoaRepository.save(pessoa);

        // Redireciona para a página "index" após salvar
        return "redirect:/index";
    }

    private Pessoa convertPessoaDTOToPessoa(PessoaDTO pessoaDTO) {
        Pessoa pessoa = new Pessoa();
        pessoa.setNome(pessoaDTO.getNome());
        pessoa.setCpf(pessoaDTO.getCpf());
        pessoa.setSenha(pessoaDTO.getSenha());
        pessoa.setConfirmarSenha(pessoaDTO.getConfirmarSenha());
        // Outros campos...

        return pessoa;
    }

    @GetMapping("/app")
    public String mostrarAppPage() {
        return "app";
    }

    @GetMapping("/index")
    public String mostrarIndexPage() {
        return "index";
    }
}
