-- The script lists number of records with same score in `second_table` of...
-- `hbtn_0c_0` database and groups them together
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
