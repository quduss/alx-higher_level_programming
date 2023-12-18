-- script that lists all tv shows with no genres in the database hbtn_0d_tvshows
SELECT title, genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON id = show_id
WHERE genre_id IS NULL
ORDER BY title, genre_id;
