-- File: 13-change_class.sql
-- Description: This script removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0.

-- Delete records with score <= 5
DELETE FROM second_table
WHERE score <= 5;

