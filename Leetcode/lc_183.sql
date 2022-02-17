select name Customers
from Customers
where id NOT IN (select distinct customerId from Orders)