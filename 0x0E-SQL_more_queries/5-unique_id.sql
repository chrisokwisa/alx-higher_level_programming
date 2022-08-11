-- creates the table unique_id on my server
-- unique_id desc, id INT with the defa
CREATE TABLE IF NOT EXISTS unique_id(
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256))
