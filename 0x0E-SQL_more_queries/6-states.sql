-- The script creates databas 'hbtn_0d_usa' and table 'states' in the...
-- database 'hbtn_0d_usa' on a MySQL server
-- fields:
-- * id INT UNIQUE NOT NULL AUTO GENERATED PRIMARY KEY
-- * name VARCHAR(256) NOT NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id	INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE,
	name	VARCHAR(256) NOT NULL
);

