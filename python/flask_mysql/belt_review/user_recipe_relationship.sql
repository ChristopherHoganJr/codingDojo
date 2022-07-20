-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema recipes_assignment
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `recipes_assignment` ;

-- -----------------------------------------------------
-- Schema recipes_assignment
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `recipes_assignment` DEFAULT CHARACTER SET utf8 ;
USE `recipes_assignment` ;

-- -----------------------------------------------------
-- Table `recipes_assignment`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipes_assignment`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipes_assignment`.`recipe`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipes_assignment`.`recipe` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `description` VARCHAR(255) NULL,
  `instructions` DATETIME NULL,
  `date` DATE NULL,
  `under_30` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recipes_assignment`.`user_has_recipe`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipes_assignment`.`user_has_recipe` (
  `user_id` INT NOT NULL,
  `recipe_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `recipe_id`),
  INDEX `fk_user_has_recipe_recipe1_idx` (`recipe_id` ASC) VISIBLE,
  INDEX `fk_user_has_recipe_user_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_has_recipe_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `recipes_assignment`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_recipe_recipe1`
    FOREIGN KEY (`recipe_id`)
    REFERENCES `recipes_assignment`.`recipe` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;