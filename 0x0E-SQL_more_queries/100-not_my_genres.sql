-- This script lists all genres not linked to the show 'Dexter'
-- Each record displays the tv_genres.name column
-- Results are sorted in ascending order by genre name
SELECT tg.name
FROM tv_genres tg
WHERE NOT EXISTS (
	SELECT 1
	FROM tv_show_genres tsg
	JOIN tv_shows ts ON tsg.show_id = ts.id
	WHERE tsg.genre_id = tg.id AND ts.title = 'Dexter'
)
ORDER BY name ASC;
