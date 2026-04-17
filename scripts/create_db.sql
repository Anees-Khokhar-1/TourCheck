-- create db script
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE subcategories (
    id SERIAL PRIMARY KEY,
    category_id INT REFERENCES categories(id),
    name TEXT,
    UNIQUE(category_id, name)
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT,
    category_id INT,
    subcategory_id INT,
    tags TEXT[],
    price FLOAT,
    currency TEXT,
    embedding VECTOR(384)
);
