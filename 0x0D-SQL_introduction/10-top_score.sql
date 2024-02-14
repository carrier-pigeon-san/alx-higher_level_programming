-- The script lists all records of the second table of database hbtn_0c_0...
-- in a MySQL server
-- Records ordered by score top first
-- The database will be passed as an argument of mysql function command as:
-- * cat 10-top_score.sql | mysql -h localhost -u root -p <database>
SELECT score, name FROM second_table ORDER BY score DESC;
