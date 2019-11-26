-- script that lists all cities in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
     ON states.id = cities.id
ORDER BY cities.id ASC;
