-- This script lists all shows, and all genres linked to that show from...
-- 'hbtn_0d_tvshows' database
-- Shows without genres will display NULL
-- Columns displayed: tv_shows.title, tv_genres.name
-- Results sorted in ascending order by the show title and genre name
SELECT ts.title, tg.name
FROM tv_shows ts
LEFT JOIN (tv_show_genres tsg, tv_genres tg)
ON (ts.id = tsg.show_id AND tsg.genre_id = tg.id)
ORDER BY title, tg.name ASC;
