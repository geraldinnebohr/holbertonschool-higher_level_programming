-- script that list all records of the table second_table
SELECT score, name FROM second_table
WHERE name is NOT NULL
ORDER BY score DESC;
