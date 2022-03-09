-- 14. my genres
-- Lists all the genres of a given tv show
SELECT g.name FROM tv_shows AS s
INNER JOIN tv_show_genres AS sg
ON sg.show_id = s.id
INNER JOIN tv_genres AS g
ON g.id = sg.genre_id
WHERE s.title = "Dexter"
ORDER BY g.name ASC;
