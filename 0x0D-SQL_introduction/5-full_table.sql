-- File: 5-full_table.sql
-- Description: This script prints the full description of the table first_table from the database hbtn_0c_0.

-- Select the full table creation statement from information_schema


-- Select column information from information_schema
SELECT * FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
SELECT * FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';

