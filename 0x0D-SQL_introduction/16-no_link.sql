-- This script lists all records of `second_table` of `hbtn_0c_0` database
-- Rows without name values are not listed
-- Records are ordered by score in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
