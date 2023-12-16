-- creates user user_0d_1 if it doesn't exist and changes its password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
ALTER USER 'user_0d_1'@'localhost' BY 'user_0d_1_pwd';
