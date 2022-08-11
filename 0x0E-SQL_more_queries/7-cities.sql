-- creates the database hbtn_0d_usa and table cities
-- in the database_0d_usa) on your server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0_usa.cities(
id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCES statese(id))
