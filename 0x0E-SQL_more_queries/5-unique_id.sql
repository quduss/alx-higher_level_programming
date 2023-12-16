-- Creates table unique_id if it doesn't exist with id and name fields. The default value id field is 1
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
