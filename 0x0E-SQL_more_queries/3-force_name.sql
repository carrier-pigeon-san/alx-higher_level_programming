-- The script creates the table 'force_name' on a MySQL server
-- fields:
-- * id - INT
-- * name - VARCHAR(256) NOT NULL
-- the database name wil be passed as an argument in the mysql command as:
-- cat 3-force_name.sql | mysql -h localhost -u root -p <database>
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
