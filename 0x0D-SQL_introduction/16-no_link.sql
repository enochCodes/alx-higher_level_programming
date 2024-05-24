-- File: 16-no_link.sql
-- Description: This script lists all records of the table second_table of the database hbtn_0c_0, excluding rows without a name value.
-- Results are displayed by score and name in descending score order.

-- List all records with non-null name ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

