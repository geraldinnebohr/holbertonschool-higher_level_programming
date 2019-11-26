-- script that creates a database and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
       id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
       state_id INT NOT NULL FOREIGN KEY(states_id) REFERENCES states(id)
       name  VARCHAR(256) NOT NULL
);
