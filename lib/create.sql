-- create.sql

-- Create the Bears table
CREATE TABLE IF NOT EXISTS bears (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    sex TEXT,
    alive INTEGER
);
