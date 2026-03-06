-- creates the MySQL server user user_0d_1
-- the user is created with the password user_0d_1_pwd
-- the user is allowed to connect from localhost only

CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- grants all privileges to the user user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;