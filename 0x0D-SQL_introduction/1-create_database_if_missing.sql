-- File: create_database.sql
-- Description: This script creates a new database named 'my_new_database' without creating any tables.

-- Start a transaction
START TRANSACTION;

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS my_new_database;

-- Commit the transaction
COMMIT;

