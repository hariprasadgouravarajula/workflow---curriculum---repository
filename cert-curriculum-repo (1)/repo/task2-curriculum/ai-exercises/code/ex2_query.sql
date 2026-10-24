SELECT dept, ROUND(AVG(score), 2) AS avg_score
FROM results
GROUP BY dept
HAVING COUNT(*) >= 3
ORDER BY avg_score DESC
LIMIT 2;
