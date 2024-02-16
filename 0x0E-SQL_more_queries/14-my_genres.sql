-- This script lists all genres of the show 'Dexter' from 'hbtn_0d_tvshows'...
-- database
-- Columns to display: name
-- Results sorted in ascending order by genre name
SELECT name
FROM tv_genres tg
JOIN (tv_show_genres tsg, tv_shows ts)
ON (tg.id = tsg.genre_id AND tsg.show_id = ts.id)
WHERE ts.title = 'Dexter'
ORDER BY name ASC
