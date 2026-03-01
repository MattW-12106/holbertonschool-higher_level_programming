-- lists top score (top to bottom) of all records in second_table
SELECT score AS top_score
FROM second_table
ORDER BY score DESC
LIMIT 1;