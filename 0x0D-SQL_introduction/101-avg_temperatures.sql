-- avg temperatures
-- orders the average temperatures of city in descending order
SELECT city, AVG(value) as avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
