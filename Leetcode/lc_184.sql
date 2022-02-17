with rn as (
select name, departmentId, salary, DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER by Salary DESC) AS rn
from Employee
)
select d.name Department,
r.name Employee,
r.salary Salary

from rn r
join Department d on r.departmentId = d.id
where r.rn = 1