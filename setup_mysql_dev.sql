-- A database hbnb_dev_db
-- A new user hbnb_dev (in localhost)
-- The password of hbnb_dev should be set to hbnb_dev_pwd
-- hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
-- hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
-- If the database hbnb_dev_db or the user hbnb_dev already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

CREATE TABLE IF NOT EXISTS users (
    email VARCHAR(128) NOT NULL,
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(128),
    last_name VARCHAR(128),
)
CREATE TABLE IF NOT EXISTS states (
    id varchar(60) NOT NULL,
    created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name VARCHAR(128) NOT NULL,
    PRIMARY KEY (name),
    PRIMARY KEY (id)
)

CREATE TABLE IF NOT EXISTS cities (
    id varchar(60) NOT NULL,
    created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name VARCHAR(128) NOT NULL,
    state_id VARCHAR(60) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(name),
    PRIMARY KEY (id)
)