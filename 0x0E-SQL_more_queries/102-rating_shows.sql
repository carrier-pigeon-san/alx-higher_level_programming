-- This script lists all shows from hbtn_0d_tvshows_rate database by their...
-- rating
-- Each record displays the columns: tv_shows.title, rating
-- Results are sorted in descending order by ratings
SELECT
	ts.title,
	SUM(tsr.rate) AS rating
FROM tv_shows ts
JOIN tv_show_ratings tsr ON tsr.show_id = ts.id
GROUP BY ts.title
ORDER BY rating DESC
