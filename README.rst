Title: Blog App
======

Description:
=============
    An admin should be able to add blog posts. Blog posts have a unique random identifier, a title and plain text where paragraphs are separated by two new-line characters.

    A viewer should be able to view all blog posts (list-mode) starting with first 5 and then the next 5 and so on. This view will not have any comments.

    A viewer should be able to click on one of these blogs to view it in full-mode. In full-mode, all past comments on the text are visible next to the text. Also, the viewer is able to comment on a paragraph of text. In essence, the comment is on a paragraph.

 APIs:
 1.) base_url/blogs         			POST          create_blog
 2.) base_url/blogs?offset    	 		GET           read_blogs (Read blogs in block of 5.)
 3.) base_url/blogs?id 	  	   			GET           read_blog
 4.) base_url/blogs/{:bid}/comments     POST          create_comment(Create comment for particular bid)
 5.) base_url/blogs/{:bid}/comments     GET           read_comments(Read all comments for particular bid)

Imp files: 1.)app/app.py
		   2.)views.py(request entry point)
		   3.)common/backup.sql
		   4.) blog.ini(configuration file)
		   5.) __init__.py (code entry point)


Description: 
a.)views (request handling) and apps (main backend logic)
b.)2 types of logs app logs and access_logs
c.)2 imp tables blogs and comments
d.) Post request payload should be in proper json format
e.) Response Json,containing 2 fields status:https_code ,msg:description and data 
{"status": 201, "msg": "Blog created successfully", "bid": "vq0a5cnivkf3er3", "timeCreated": "2017-03-15 14:52:54"}

Technology Used:
Pyramid, Cornice,Sqlalchemy

DB Schema:
	CREATE DATABASE blog_db;
	USE blog_db;

	CREATE TABLE IF NOT EXISTS `blog` (
    	`id` CHAR(15) NOT NULL,
    	`creator` VARCHAR(31) NOT NULL,
    	`headline` VARCHAR(31) NOT NULL,
    	`text` TEXT NOT NULL,
    	`timeCreated` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    	PRIMARY KEY (`id`),
    	INDEX (`timeCreated`)
    );


	CREATE TABLE IF NOT EXISTS `comment` (
    	`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    	`bid` CHAR(15) NOT NULL,
    	`position` INT NOT NULL,
    	`creator` VARCHAR(31) NOT NULL,
    	`text` TEXT NOT NULL,
    	`timeCreated` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    	PRIMARY KEY (`id`),
    	FOREIGN KEY (`bid`) REFERENCES `blog`(`id`),
    	INDEX (`timeCreated`)
    );

How to install?
sudo apt-get install python-pyramid
sudo apt-get install python-virtualenv
sudo apt-get install libmysqlclient-dev
sudo apt-get install python-dev

cd projects
virtualenv env
clone blog repo here

../env/bin/python setup.py develop
../env/bin/pserve blog.ini --reload


Sample requests:

curl 0.0.0.0:6543/blogs -d '{"creator":"Atul Kumar", "headline" : "Reality: Illusion" ,"text":"Whatever we see almost everything is an illusion"}' -H "Content-Type: application/json"

curl 0.0.0.0:6543/blogs
curl 0.0.0.0:6543/blogs?offset=2
curl 0.0.0.0:6543/blogs?id=3

curl 0.0.0.0:6543/blogs/f6dkaoon949i9go/comments -d '{"creator":"Atul Kumar" ,"text":"Stop Commenting","position":4}' -H "Content-Type: application/json"

curl 0.0.0.0:6543/blogs/f6dkaoon949i9go/comments 


For Logs:
cd blog
mkdir -p logs/access_logs
mkdir -p logs/api_logs
chmod -R 777 logs


Author: Atul kumar(atul.kumar0401@gmail.com)