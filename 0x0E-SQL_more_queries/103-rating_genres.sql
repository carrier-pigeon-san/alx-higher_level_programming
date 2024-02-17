-- This script lists all genres in the database .hbtn_0d_tvshows_rate'...
-- database
-- Each record displays columns: tv_shows.name, rating
-- Results are sorted in descending order by their rating
SELECT
	tg.name,
	SUM(tsr.rate) AS rating
FROM tv_genres tg
JOIN tv_show_genres tsg ON tsg.genre_id = tg.id
JOIN tv_shows ts ON ts.id = tsg.show_id
JOIN tv_show_ratings tsr ON tsr.show_id = ts.id
GROUP BY tg.name
ORDER BY rating DESC;
