-- lists all the cities of california
-- that can be found in the database
SELECT id, name FROM cities WHERE state_id = (
WHERE name = 'California')
ORDER BY id ASC;
