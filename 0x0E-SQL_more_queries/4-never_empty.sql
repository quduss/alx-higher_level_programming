-- creates table id_not_null with id and name fields. The default value of the id field is 1.
CREATE TABLE IF NOT EXISTS id_not_null (
id INT DEFAULT 1,
name VARCHAR(256)
);
