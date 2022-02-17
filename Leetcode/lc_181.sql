select e.name Employee
from Employee e
inner join Employee e2 on e.managerId = e2.Id 
where e.salary > e2.salary
-- trick is to create a table for employees with managers and compare on the spot