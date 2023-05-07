CREATE DATABASE IF NOT EXISTS users;

USE users;

CREATE TABLE users (
  id INT PRIMARY KEY,
  username VARCHAR(50),
  password VARCHAR(50)
);
