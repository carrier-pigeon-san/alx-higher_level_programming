-- This script removes all records that have a value <= 5 in the 'score' field
-- The database name will be passed as an argument of the `mysql` command as:
-- * cat 13-no_link.sql | mysql -h localhost -u root -p <database>
DELETE FROM second_table WHERE score <= 5;
