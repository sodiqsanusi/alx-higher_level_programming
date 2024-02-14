-- List from the table the count of some values, and sort them according to mode
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
