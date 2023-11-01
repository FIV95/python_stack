-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema cars
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cars
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cars` DEFAULT CHARACTER SET utf8 ;
USE `cars` ;

-- -----------------------------------------------------
-- Table `cars`.`cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cars`.`cars` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `brand` VARCHAR(45) NULL,
  `model` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cars`.`owners`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cars`.`owners` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first` VARCHAR(45) NULL,
  `last` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cars`.`garages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cars`.`garages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `quality` VARCHAR(45) NULL,
  `car_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_garages_cars1_idx` (`car_id` ASC) VISIBLE,
  CONSTRAINT `fk_garages_cars1`
    FOREIGN KEY (`car_id`)
    REFERENCES `cars`.`cars` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cars`.`cars_owners`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cars`.`cars_owners` (
  `cars_id` INT NOT NULL,
  `owners_id` INT NOT NULL,
  PRIMARY KEY (`cars_id`, `owners_id`),
  INDEX `fk_cars_has_owners_owners1_idx` (`owners_id` ASC) VISIBLE,
  INDEX `fk_cars_has_owners_cars_idx` (`cars_id` ASC) VISIBLE,
  CONSTRAINT `fk_cars_has_owners_cars`
    FOREIGN KEY (`cars_id`)
    REFERENCES `cars`.`cars` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cars_has_owners_owners1`
    FOREIGN KEY (`owners_id`)
    REFERENCES `cars`.`owners` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
