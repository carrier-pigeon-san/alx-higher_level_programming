-- The script creates database 'hbtn_0d_usa' and table 'cities' in the...
-- database 'hbtn_0d_usa' on a MySQL server
-- fields:
-- * id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE
-- * state_id INT NOT NULL FOREIGN KEY to id of the states table
-- * name VARCHAR(256) NOT NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,

	FOREIGN KEY (state_id)
	  REFERENCES states(id)
);

