-- File: 11-best_score.sql
-- Description: This script lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0.
-- The results display both the score and the name in this order, ordered by score (top first).

-- Select score and name from second_table where score >= 10, ordered by score descending
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

