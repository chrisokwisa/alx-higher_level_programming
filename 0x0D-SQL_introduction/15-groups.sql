-- lists the number of records with the same score
-- list should be sorted by the number of records
SELECT score, count(*) as number FROM second_table
GROUP BY score ORDER BY number DESC;
