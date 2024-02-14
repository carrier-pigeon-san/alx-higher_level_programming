-- The script displays number of records with id = 89 in...
-- table `first_table` of `hbtn_0c_0` database in a MySQL server
-- The database name will be passed as an argumenrt of the mysql command as:
-- * cat 8-count_89.sql | mysql -h localhost -u root -p <database>
SELECT COUNT(*)
FROM first_table
WHERE id IN (SELECT id FROM first_table WHERE id = 89);
