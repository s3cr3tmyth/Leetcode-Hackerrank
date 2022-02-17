-- nothing to self join so select from multiple works here
SELECT w1.id FROM Weather w1, Weather w2
WHERE DATEADD(day, -1, w1.recordDate) = w2.recordDate AND w1.temperature > w2.temperature