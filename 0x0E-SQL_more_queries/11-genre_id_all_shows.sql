-- A script that lists all shows in 'hbtn_0d_tvshows' database
-- Shows without genres will display NULL
-- Columns displayed: tv_shows.title, tv_shows_genres.genre_id
-- Sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT ts.title, tsg.genre_id
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
ORDER BY title, tsg.genre_id ASC
