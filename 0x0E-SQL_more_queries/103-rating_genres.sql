-- 103. rate by genre
-- Lists all the genres by their rating
SELECT g.name, SUM(sr.rate) AS rating FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg
ON sg.genre_id = g.id
INNER JOIN tv_shows AS s
ON s.id = sg.show_id
INNER JOIN tv_show_ratings AS sr
ON sr.show_id = s.id
GROUP BY g.name
ORDER BY rating DESC;
