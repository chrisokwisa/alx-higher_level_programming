-- lists all records of the second_table
-- database hbtn_0c_0
SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
