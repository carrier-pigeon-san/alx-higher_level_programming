-- The script creates a MySQL server user user_0d_1 who:
-- * has all privileges on the MySQL server
-- * has the password set to user_0d_1_pwd
-- The script does not fail if the user already exists
CREATE USER
IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
ON *.*
TO 'use_0d_1'@'localhost' 
WITH GRANT OPTION;
