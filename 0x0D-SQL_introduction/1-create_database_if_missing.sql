-- File: create_database.sql
-- Description: This script creates a new database named 'my_new_database' if it does not already exist.

-- Check if the database already exists
SELECT SCHEMA_NAME
FROM INFORMATION_SCHEMA.SCHEMATA
WHERE SCHEMA_NAME = 'hbtn_0c_0';

-- If the database does not exist, createt
CREATE DATABASE IF NOT EXISTS my_new_database;

