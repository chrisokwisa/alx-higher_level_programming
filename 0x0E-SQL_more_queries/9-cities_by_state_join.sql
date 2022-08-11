-- lists all cities contained in hbtn_0d_usa
-- display: cities.id - cities.name - states.name
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
