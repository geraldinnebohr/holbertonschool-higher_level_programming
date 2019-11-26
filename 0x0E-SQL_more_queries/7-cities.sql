-- script that creates a database and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
       id INT PRIMARY KEY,
       state_id INT FOREIGN KEY(id.states)
       name  VARCHAR(256) NOT NULL
);
