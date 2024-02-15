-- This script lists all the cities contained the database hbtn_0d_usa
-- Each record to display cities.id - cities.name - states.name
-- Results sortes in ascending order by cities.id
SELECT c.id, c.name, s.name
FROM cities c
  JOIN states s
    ON c.state_id = s.id 
      ORDER BY id ASC;
