-- This script list all shows not linked to the 'comedy' genre in...
-- 'hbtn_0d_tvshows' database
-- Each record displays the tv_shows.title column
-- Results are sorted in ascending order by the show title
SELECT ts.title
FROM tv_shows ts
WHERE NOT EXISTS (
	SELECT 1
	FROM tv_show_genres tsg
	JOIN tv_genres tg ON tsg.genre_id = tg.id
	WHERE tsg.show_id = ts.id AND tg.name = 'Comedy'
)
ORDER BY title ASC;
