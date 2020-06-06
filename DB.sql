CREATE SCHEMA `finaltest` ;
#创建数据库

CREATE TABLE `finaltest`.`auther_user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `sex` VARCHAR(2) NULL DEFAULT NULL,
  `job` VARCHAR(45) NULL DEFAULT NULL,
  `age` INT NULL DEFAULT NULL,
  `like` VARCHAR(45) NULL DEFAULT NULL,
  `power` INT NOT NULL DEFAULT '0',
  `password` VARCHAR(45) NOT NULL,
  `salt` VARCHAR(20) NULL DEFAULT NULL,
  `cookie` VARCHAR(45) NULL DEFAULT NULL,
  `updated` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));
#创建user表

CREATE TABLE `finaltest`.`article_post` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NOT NULL,
  `body` TEXT NOT NULL,
  `author_id` INT NOT NULL,
  `privacy` INT NOT NULL,
  `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `auther_article_idx` (`author_id` ASC) VISIBLE,
  CONSTRAINT `auther_article`
    FOREIGN KEY (`author_id`)
    REFERENCES `finaltest`.`auther_user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);
#创建文章表

CREATE TABLE `finaltest`.`answer_review` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `reviewText` TEXT NOT NULL,
  `questionID_id` INT NOT NULL,
  `writerID_id` INT NOT NULL,
  `helpfulVote` INT NOT NULL DEFAULT '0',
  `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `auther_review_new_idx` (`writerID_id` ASC) VISIBLE,
  INDEX `question_review_idx` (`questionID_id` ASC) VISIBLE,
  CONSTRAINT `auther_review_new`
    FOREIGN KEY (`writerID_id`)
    REFERENCES `finaltest`.`auther_user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `question_review`
    FOREIGN KEY (`questionID_id`)
    REFERENCES `finaltest`.`article_post` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);
#创建评论表

CREATE TABLE `finaltest`.`answer_review_users_like` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `review_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `1_idx` (`review_id` ASC) VISIBLE,
  INDEX `2_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `1`
    FOREIGN KEY (`review_id`)
    REFERENCES `finaltest`.`answer_review` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `2`
    FOREIGN KEY (`user_id`)
    REFERENCES `finaltest`.`auther_user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);
#创建喜爱关系表

CREATE VIEW `cookie` AS
select `id`,`cookie` from `finaltest`.`auther_user`;
#创建cookie视图

CREATE USER 'login' IDENTIFIED BY 'login_password'; 
CREATE USER 'signup' IDENTIFIED BY 'signup_password'; 
CREATE USER 'userinfo' IDENTIFIED BY 'userinfo_password'; 
CREATE USER 'userchange' IDENTIFIED BY 'userchange_password'; 
CREATE USER 'userpowerup' IDENTIFIED BY 'userpowerup'; 

GRANT select,update ON auther_user TO 'login';
GRANT insert ON auther_user TO 'signup';
GRANT select ON auther_user TO 'userinfo';
GRANT update ON auther_user TO 'userchange';
GRANT update ON auther_user TO 'userpowerup';
#创建需要的功能用户并授权