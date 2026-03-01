-- lists top score (top to bottom) of all records in second_table
SELECT score, NAMES
FROM second_table
ORDER BY score DESC;