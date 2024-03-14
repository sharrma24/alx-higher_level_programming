-- Records are ordered by descending score.
-- Lists all records of the table second_table with a value in  MySQL server.
FROM `second_table`
SELECT `score`, `name`
WHERE `name` != ""
ORDER BY `score` DESC
