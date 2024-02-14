-- script creates table 'second_table' in current database in a MySQL server
-- fields:
-- * id - INT
-- * name - VARCHAR(256)
-- * score - INT
-- database name is passed as an argument of the `mysql` command as:
-- * cat 4-first_table.sql | mysql -h localhost - u root <database>
-- script should not fail if given table already exists
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
INSERT INTO second_table (id, name, score)
	VALUES ('1', 'John', '10'), ('2', 'Alex', '3'), ('3', 'Bob', '14'), ('4', 'George', '8');
