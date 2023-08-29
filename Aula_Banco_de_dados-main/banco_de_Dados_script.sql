-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Padel_bd
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Padel_bd
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Padel_bd` DEFAULT CHARACTER SET utf8 ;
USE `Padel_bd` ;

-- -----------------------------------------------------
-- Table `Padel_bd`.`Jogador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Padel_bd`.`Jogador` (
  `idJogador` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `apelido` INT NULL,
  `posicao` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idJogador`),
  INDEX `iNDEX` (`nome` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Padel_bd`.`torneio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Padel_bd`.`torneio` (
  `idtorneio` INT NOT NULL AUTO_INCREMENT,
  `clube` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idtorneio`),
  INDEX `INDEX` (`clube` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Padel_bd`.`Jogador_torneio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Padel_bd`.`Jogador_torneio` (
  `idJogador_torneio` INT NOT NULL AUTO_INCREMENT,
  `idJogador_1` INT NOT NULL,
  `idJogador_2` INT NOT NULL,
  `idtorneio` INT NOT NULL,
  PRIMARY KEY (`idJogador_torneio`),
  INDEX `fk_Jogador_torneio_Jogador_idx` (`idJogador_1` ASC) VISIBLE,
  INDEX `fk_Jogador_torneio_Jogador1_idx` (`idJogador_2` ASC) VISIBLE,
  INDEX `fk_Jogador_torneio_torneio1_idx` (`idtorneio` ASC) VISIBLE,
  CONSTRAINT `fk_Jogador_torneio_Jogador`
    FOREIGN KEY (`idJogador_1`)
    REFERENCES `Padel_bd`.`Jogador` (`idJogador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Jogador_torneio_Jogador1`
    FOREIGN KEY (`idJogador_2`)
    REFERENCES `Padel_bd`.`Jogador` (`idJogador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Jogador_torneio_torneio1`
    FOREIGN KEY (`idtorneio`)
    REFERENCES `Padel_bd`.`torneio` (`idtorneio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
