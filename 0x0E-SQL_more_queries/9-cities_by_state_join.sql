-- This script lists all the cities contained the database hbtn_0d_usa
-- Each record to display cities.id - cities.name - states.name
-- Results sortes in ascending order by cities.id
SELECT id, cities.name, states.name
FROM cities
  INNER JOIN states
    ON cities.state_id = states.id ORDER BY id ASC;
