-- script creates table 'first_table' in current database in a MySQL server
-- fields:
-- * id - INT
-- * name - VARCHAR(256)
-- database name is passed as an argument of the `mysql` command as:
-- * cat 4-first_table.sql | mysql -h localhost - u root <database>
-- script should not fail if given table already exists
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
