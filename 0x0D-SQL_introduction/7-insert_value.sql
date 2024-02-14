-- The script inserts a new row in the table `first_table` in the...
-- `hbtn_0c_0` database in a MySQL server
-- New row:
-- * id = 89
-- * name = Best School
-- The database name will be passed as an argument of the `mysql` command as:
-- * cat 7-insert_value.sql | mysql -h localhost -u root -p <database>
INSERT INTO first_table (
	id,
	name
) VALUES (
	'89',
	'Best School'
);
	
