Select department_id, avg(salary) as avg_salary From employees group by department_id Order by avg_salary desc
limit 1;
