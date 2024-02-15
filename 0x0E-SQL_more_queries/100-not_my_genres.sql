-- a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT DISTINCT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.show_id IS NULL
   OR tv_show_genres.show_id NOT IN (SELECT id FROM tv_shows WHERE title = 'Dexter')
ORDER BY tv_genres.name ASC;
