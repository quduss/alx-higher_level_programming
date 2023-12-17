-- script that lists all shows contained in the database hbtn_0d_tvshows
SELECT title, genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON id = show_id
ORDER BY title, genre_id;
