-- Records are ordered by descending.
-- Lists all records in the table second_table with a score >= 10 in my MySQL server.
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
FROM `second_table`
