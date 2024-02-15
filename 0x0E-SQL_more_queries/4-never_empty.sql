-- The script creates the table 'id_not_null' on a MySQL server
-- fields:
-- * id - INT default value = 1
-- * name - VARCHAR(256)
-- the database name wil be passed as an argument in the mysql command as:
-- cat 4-never_empty.sql | mysql -h localhost -u root -p <database>
CREATE TABLE IF NOT EXISTS id_not_null (
	id	INT DEFAULT 1,
	name	VARCHAR(256)
);
