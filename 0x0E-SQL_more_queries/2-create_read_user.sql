-- The scripts creates a database hbtn_0d_2 and user user_0d_2
-- user_0d_2 is granted only SELECT privileges database hbtn_0d_2
-- user_0d_@ password is set to user_0d_2_pwd
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2
IDENTIFIED BY user_0d_2_pwd;
GRANT SELECT
ON hbtn_0d_2.*
TO user_0d_2;
