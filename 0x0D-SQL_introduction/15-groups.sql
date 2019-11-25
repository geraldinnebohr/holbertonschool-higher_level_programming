-- script that list # of records with same score in the table second_table
SELECT score, COUNT(*) number
FROM second_table GROUP BY score
HAVING number >= 1
ORDER BY score DESC;
