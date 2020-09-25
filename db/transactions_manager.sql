DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS merchants;


CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    budget INT
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    tag_id INT REFERENCES tags(id) ON DELETE CASCADE,
    merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
    amount INT,
    date DATE NOT NULL

);
