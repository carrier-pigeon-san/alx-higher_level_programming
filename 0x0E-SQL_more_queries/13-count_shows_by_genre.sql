-- This script lists all genres from 'hbtn_0d_tvshows' database and shows...
-- the number of shows linked to each
-- Columns to display: <TV Show genre, <Number of shows linked to this genre>
-- First column alias 'genre'
-- Second column alias 'number of shows'
-- Genres without shows linked are not listed
SELECT tg.name AS genre, COUNT(tsg.genre_id) AS number_of_shows
FROM tv_genres tg
JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
GROUP BY tsg.genre_id
ORDER BY number_of_shows DESC
