-- script that creates a database and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
       id INT NOT NULL UNIQUE AUTO_INCREMENT,
       state_id INT NOT NULL,
       name  VARCHAR(256) NOT NULL,
       PRIMARY KEY(id),
       FOREIGN KEY(states_id) REFERENCES states(id)
);
