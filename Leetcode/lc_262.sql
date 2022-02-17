SELECT t.request_at Day,
CAST
(
    CAST(count(distinct case when t.status IN ('cancelled_by_driver', 'cancelled_by_client') then t.id end) AS FLOAT) / 
    CAST(count(distinct t.id) AS FLOAT) 
    AS decimal(10, 2)
)
[Cancellation Rate]

FROM Trips t
JOIN Users AS u1 on u1.users_id = t.client_id and u1.banned = 'No'
JOIN Users AS u2 on u2.users_id = t.driver_id and u2.banned = 'No'

WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at