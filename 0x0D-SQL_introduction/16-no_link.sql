-- Lists all records in teh table with restrictions on what to list
SELECT score, name from second_table
WHERE name IS NOT NULL AND name != ""
ORDER BY score DESC;
