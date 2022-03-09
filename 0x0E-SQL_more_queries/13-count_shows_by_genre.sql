-- 13. shows by genre count
-- Counts the ammount of shows in each genre
SELECT g.name AS genre, COUNT(*) AS number_of_shows FROM tv_genres AS g
INNER JOIN tv_show_genres AS s
ON s.genre_id = g.id
GROUP BY g.name
ORDER BY number_of_shows DESC;
