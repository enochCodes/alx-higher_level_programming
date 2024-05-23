-- File: 10-top_score.sql
-- Description: This script lists all records of the table second_table of the database hbtn_0c_0.
-- The results display both the score and the name in this order, ordered by score (top first).

-- Select score and name from second_table, ordered by score descending
SELECT score, name
FROM second_table
ORDER score > 10 BY DESC;

