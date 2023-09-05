-- seed.sql

-- Create the Bears table
CREATE TABLE IF NOT EXISTS bears (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    sex TEXT,
    alive INTEGER
);

-- Insert sample data into the Bears table
INSERT INTO bears (name, age, sex, alive) VALUES
    ('Bear1', 5, 'M', 1),
    ('Bear2', 3, 'F', 1),
    ('Bear3', 8, 'M', 0);
