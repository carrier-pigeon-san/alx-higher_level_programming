-- This scripts lists all cities of California found in the 'hbtn_0d_usa'...
-- database
-- Results are sorted in ascending irder by cities.id
SELECT id, name
FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = 'California')
