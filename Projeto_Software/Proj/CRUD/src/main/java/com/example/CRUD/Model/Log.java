package com.example.CRUD.Model;
import jakarta.persistence.*;
import lombok.Getter;
import java.util.Date;
@Getter
@Entity
public class Log {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer id;

    @ManyToOne
    @JoinColumn(name = "usuario_id", nullable = false)
    private Pessoa Pessoa;

    @Temporal(TemporalType.TIMESTAMP)
    @Column(nullable = false)
    private Date dataAcao;

    @Column(nullable = false)
    private String acaoRealizada;

    public void setId(Integer id) {
        this.id = id;
    }

    public void setPessoa(Pessoa pessoa) {
        this.Pessoa = pessoa;
    }

    public void setDataAcao(Date dataAcao) {
        this.dataAcao = dataAcao;
    }

    public void setAcaoRealizada(String acaoRealizada) {
        this.acaoRealizada = acaoRealizada;
    }
}
