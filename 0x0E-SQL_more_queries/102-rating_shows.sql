-- 102. Im a critic now
-- Lists all the shows and their accumulate rating in descending order
SELECT s.title, SUM(sr.rate) AS rating FROM tv_shows AS s
RIGHT JOIN tv_show_ratings AS sr
ON sr.show_id = s.id
GROUP BY s.title
ORDER BY rating DESC;
