-- File: 3-list_tables.sql
-- Description: This script lists all tables in the specified MySQL database.

-- Ensure the database name is passed as an argument
USE `mysql`;

-- Query to retrieve table names
SELECT TABLE_NAME AS Tables_in_mysql
FROM information_schema.tables
WHERE TABLE_SCHEMA = 'mysql';

