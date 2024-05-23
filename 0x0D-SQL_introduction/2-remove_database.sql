-- File: 2-remove_database.sql
-- Description: This script attempts to drop the database named 'hbtn_0c_0' if it already exists.

-- Start a transaction
START TRANSACTION;

-- Drop the database if it exists
DROP DATABASE IF EXISTS hbtn_0c_0;

-- Commit the transaction
COMMIT;

