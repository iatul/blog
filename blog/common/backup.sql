CREATE DATABASE blog_db;
USE blog_db;

CREATE TABLE IF NOT EXISTS `blog` (
  	`id` CHAR(15) NOT NULL,
    `creator` VARCHAR(31) NOT NULL,
    `headline` VARCHAR(31) NOT NULL,
    `text` TEXT NOT NULL,
    `dateCreated` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    INDEX (`dateCreated`)
    );


CREATE TABLE IF NOT EXISTS `comment` (
  	`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  	`bid` CHAR(15) NOT NULL,
    `position` INT NOT NULL,
    `text` TEXT NOT NULL,
    `dateCreated` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`bid`) REFERENCES `blog`(`id`),
    INDEX (`dateCreated`)
    );

