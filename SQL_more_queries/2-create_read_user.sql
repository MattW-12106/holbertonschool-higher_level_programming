-- creates the database hbtn_0d_2 and the user user_0d_2
IF NOT EXISTS CREATE DATABASE hbtn_0d_2;
IF NOT EXISTS CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'hbtn_0d_2_pwd';

-- user only has SELECT privilege on the database hbtn_0d_2
GRANT SELECT ON DATABASE hbtn_0d_2 TO 'user_0d_2'@'localhost';
