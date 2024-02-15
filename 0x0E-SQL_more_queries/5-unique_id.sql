-- The script creates the table 'unique_id' on a MySQL server
-- fields:
-- * id INT DEFAULT VALUE 1 UNIQUE
-- * name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);	
