-- File: 14-average.sql
-- Description: This script computes the score average of all records in the table second_table of the database hbtn_0c_0.
-- The result column name should be average.

-- Compute the average score
SELECT AVG(score) AS average
FROM second_table;

