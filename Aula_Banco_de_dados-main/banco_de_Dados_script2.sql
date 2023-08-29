show databases;
use padel_bd;

show tables;

CREATE TABLE Ranking (
idRanking INT NOT NULL AUTO_INCREMENT,
idjogador int NOT NULL,
pontos int not NULL,
PRIMARY KEY (idRanking),
INDEX `INDEX` (pontos DESC) VISIBLE,
CONSTRAINT `fk_Ranking_Jogador`
	FOREIGN KEY (idJogador)
    REFERENCES Jogador (idJogador)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

show tables;

select * 
FROM ranking;
