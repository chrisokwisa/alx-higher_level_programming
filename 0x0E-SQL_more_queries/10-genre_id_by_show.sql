-- lists all shows contained in hbtn_0d_tvshows
-- at least one genre linked
SELECT tv_shows.title, tv_show_genres.genres_id
FROM tv_shows
RIGHT JOIN tv_show_genres ON tv_show_genres.show_i = tv_shows.id
ORDER BY tv_shows.tit le ASC, tv_shows_genres_id ASC
