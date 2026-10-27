/* Write your T-SQL query statement below */
select min(m.name) as name from Employee e join Employee m on e.managerId=m.id
group by m.id
having count(*)>4