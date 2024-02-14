-- Lists all records in the table with restrictions

SELECT score, name from second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
