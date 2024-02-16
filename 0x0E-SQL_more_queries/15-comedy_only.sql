-- This script lists all comedy shows in 'hbtn_0d_tvshows' database
--Column(s) to display: tv_shows.title
--Results sorted in ascending order by show title
SELECT title
FROM tv_shows ts
JOIN (tv_show_genres tsg, tv_genres tg)
ON (ts.id = tsg.show_id AND tsg.genre_id = tg.id)
WHERE tg.name = 'Comedy'
ORDER BY title ASC
