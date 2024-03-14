-- Displays the max temperature of each states.
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
ORDER BY `state`;
GROUP BY `state`
