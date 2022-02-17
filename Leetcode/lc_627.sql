-- no select statemnets only update
UPDATE Salary
SET sex = (CASE WHEN sex = 'm' THEN  'f' ELSE 'm' END)
--replace(sex, 'm', 'f')