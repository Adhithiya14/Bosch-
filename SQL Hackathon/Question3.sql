Select e.employee_id, e.name, e.department_id, e.salary From employees e Where e.salary > (
    select avg(salary)
    from employees
    WHERE department_id = e.department_id
);
