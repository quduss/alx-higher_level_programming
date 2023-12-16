-- creates table force_name in the database passed as an argument with the name column not able to contain a null value
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
