-- Create by Tomas de Castro for Holberton School 2021

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id
