-- File: 15-groups.sql
-- Description: This script lists the number of records with the same score in the table second_table of the database hbtn_0c_0.
-- The result displays the score and the number of records for this score with the label number, sorted by the number of records (descending).

-- List the number of records with the same score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

