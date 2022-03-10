-- 100. not my genre
-- Lists all the genres not connected to the show
SELECT g.name FROM tv_genres AS g
WHERE g.name NOT IN (
	SELECT g.name FROM tv_shows AS s
	LEFT JOIN tv_show_genres AS sg
	ON sg.show_id = s.id
	LEFT JOIN tv_genres AS g
	ON g.id = sg.genre_id
	WHERE s.title = "Dexter"
)
ORDER BY g.name;
