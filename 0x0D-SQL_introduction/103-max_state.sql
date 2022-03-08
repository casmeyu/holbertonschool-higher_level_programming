-- max temperature
-- Displays the maximum temperature of each state
SELECT state, MAX(value) FROM temperatures
GROUP BY state
