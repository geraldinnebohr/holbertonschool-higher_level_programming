-- script that lists all shows contained in the database that
-- have at least one genre linked
SELECT tv_genres.name AS name
FROM tv_genres
JOIN tv_show_genres
     ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
     ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name;
