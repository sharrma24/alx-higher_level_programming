-- Records are ordered by descending score.
-- Lists all records of the table second_table with a value in  MySQL server.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
