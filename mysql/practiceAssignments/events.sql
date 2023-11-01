-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema event_planner_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema event_planner_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `event_planner_schema` DEFAULT CHARACTER SET utf8 ;
USE `event_planner_schema` ;

-- -----------------------------------------------------
-- Table `event_planner_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `event_planner_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `address_id` INT NOT NULL,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_addresses1_idx` (`address_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_addresses1`
    FOREIGN KEY (`address_id`)
    REFERENCES `event_planner_schema`.`addresses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `event_planner_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `event_planner_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `address_id` INT NOT NULL,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_addresses1_idx` (`address_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_addresses1`
    FOREIGN KEY (`address_id`)
    REFERENCES `event_planner_schema`.`addresses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `event_planner_schema`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `event_planner_schema`.`posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user` INT NOT NULL,
  `text` VARCHAR(45) NULL,
  `created_at` VARCHAR(45) NULL,
  `updated_at` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_posts_users1_idx` (`user` ASC) VISIBLE,
  CONSTRAINT `fk_posts_users1`
    FOREIGN KEY (`user`)
    REFERENCES `event_planner_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `event_planner_schema`.`shares`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `event_planner_schema`.`shares` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `photo_id` INT NOT NULL,
  `post_id` INT NOT NULL,
  `comments_id` INT NOT NULL,
  `count` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_shares_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_shares_photos1_idx` (`photo_id` ASC) VISIBLE,
  INDEX `fk_shares_posts1_idx` (`post_id` ASC) VISIBLE,
  INDEX `fk_shares_comments1_idx` (`comments_id` ASC) VISIBLE,
  CONSTRAINT `fk_shares_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `event_planner_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_shares_photos1`
    FOREIGN KEY (`photo_id`)
    REFERENCES `event_planner_schema`.`photos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_shares_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `event_planner_schema`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_shares_comments1`
    FOREIGN KEY (`comments_id`)
    REFERENCES `event_planner_schema`.`comments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `event_planner_schema`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `event_planner_schema`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `photo_id` INT NOT NULL,
  `share_id` INT NOT NULL,
  `post_id` INT NOT NULL,
  `text` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_comments_photos1_idx` (`photo_id` ASC) VISIBLE,
  INDEX `fk_comments_shares1_idx` (`share_id` ASC) VISIBLE,
  INDEX `fk_comments_posts1_idx` (`post_id` ASC) VISIBLE,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `event_planner_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_photos1`
    FOREIGN KEY (`photo_id`)
    REFERENCES `event_planner_schema`.`photos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_shares1`
    FOREIGN KEY (`share_id`)
    REFERENCES `event_planner_schema`.`shares` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `event_planner_schema`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `event_planner_schema`.`photos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `event_planner_schema`.`photos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `comment_id` INT NOT NULL,
  `post_id` INT NOT NULL,
  `photo` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_photos_users_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_photos_comments1_idx` (`comment_id` ASC) VISIBLE,
  INDEX `fk_photos_posts1_idx` (`post_id` ASC) VISIBLE,
  CONSTRAINT `fk_photos_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `event_planner_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_photos_comments1`
    FOREIGN KEY (`comment_id`)
    REFERENCES `event_planner_schema`.`comments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_photos_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `event_planner_schema`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `event_planner_schema`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `event_planner_schema`.`likes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `photo_id` INT NOT NULL,
  `posts_id` INT NOT NULL,
  `share_id` INT NOT NULL,
  `comment_id` INT NOT NULL,
  `count` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_likes_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_likes_photos1_idx` (`photo_id` ASC) VISIBLE,
  INDEX `fk_likes_posts1_idx` (`posts_id` ASC) VISIBLE,
  INDEX `fk_likes_shares1_idx` (`share_id` ASC) VISIBLE,
  INDEX `fk_likes_comments1_idx` (`comment_id` ASC) VISIBLE,
  CONSTRAINT `fk_likes_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `event_planner_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_photos1`
    FOREIGN KEY (`photo_id`)
    REFERENCES `event_planner_schema`.`photos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_posts1`
    FOREIGN KEY (`posts_id`)
    REFERENCES `event_planner_schema`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_shares1`
    FOREIGN KEY (`share_id`)
    REFERENCES `event_planner_schema`.`shares` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_comments1`
    FOREIGN KEY (`comment_id`)
    REFERENCES `event_planner_schema`.`comments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `event_planner_schema`.`comments_has_comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `event_planner_schema`.`comments_has_comments` (
  `comment_id` INT NOT NULL,
  `comments comment_id` INT NOT NULL,
  PRIMARY KEY (`comment_id`, `comments comment_id`),
  INDEX `fk_comments_has_comments_comments2_idx` (`comments comment_id` ASC) VISIBLE,
  INDEX `fk_comments_has_comments_comments1_idx` (`comment_id` ASC) VISIBLE,
  CONSTRAINT `fk_comments_has_comments_comments1`
    FOREIGN KEY (`comment_id`)
    REFERENCES `event_planner_schema`.`comments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_has_comments_comments2`
    FOREIGN KEY (`comments comment_id`)
    REFERENCES `event_planner_schema`.`comments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `event_planner_schema`.`addresses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `event_planner_schema`.`addresses` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `address` VARCHAR(255) NULL,
  `city` VARCHAR(255) NULL,
  `zip` INT NULL,
  `state` VARCHAR(55) NULL,
  `created_at` VARCHAR(45) NULL,
  `updated_at` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `event_planner_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `event_planner_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `address_id` INT NOT NULL,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_addresses1_idx` (`address_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_addresses1`
    FOREIGN KEY (`address_id`)
    REFERENCES `event_planner_schema`.`addresses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `event_planner_schema`.`events`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `event_planner_schema`.`events` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NULL,
  `description` TEXT(300) NULL,
  `start_time` TIME NULL,
  `end_time` TIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `event_planner_schema`.`event_addresses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `event_planner_schema`.`event_addresses` (
  `event_id` INT NOT NULL,
  `addresse_id` INT NOT NULL,
  INDEX `fk_event_addresses_events1_idx` (`event_id` ASC) VISIBLE,
  INDEX `fk_event_addresses_addresses1_idx` (`addresse_id` ASC) VISIBLE,
  CONSTRAINT `fk_event_addresses_events1`
    FOREIGN KEY (`event_id`)
    REFERENCES `event_planner_schema`.`events` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_event_addresses_addresses1`
    FOREIGN KEY (`addresse_id`)
    REFERENCES `event_planner_schema`.`addresses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
