-- script that lists all cities of California in the database hbtn_0d_usa
SELECT cities.name, cities.id FROM cities
WHERE state_id =(
      SELECT id FROM states WHERE name = 'California'
)
ORDER BY cities.id ASC;
