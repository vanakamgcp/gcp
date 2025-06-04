-- 1.Second highest salary of employees
SELECT *, DENSE_RANK() OVER (ORDER BY SALARY DESC) rnk FROM hr.employees QUALIFY rnk = 2;
-- using subquery
SELECT MAX(SALARY) FROM hr.employees WHERE salary < (SELECT MAX(SALARY) FROM hr.employees);
-- 2. Nth highest salary of employee
SELECT *, DENSE_RANK() OVER (ORDER BY SALARY DESC) rnk FROM hr.employees QUALIFY rnk = 2;
-- 3. Employees getting more than avg salary
SELECT * FROM hr.employees WHERE salary > (SELECT AVG(SALARY) FROM hr.employees);

SELECT first_name,salary,AVG(SALARY) OVER () AVG_SAL FROM hr.employees QUALIFY salary > avg_sal;

-- 4. get common records from two tables
SELECT department_id FROM hr.employees
INTERSECT DISTINCT
select department_id FROM hr.departments;

-- 5. Last 10 records from the table
SELECT * FROM hr.employees ORDER BY employee_id desc limit 10;
-- 6. Top 5 highest salaried employees
SELECT first_name,salary,DENSE_RANK() OVER (order by salary desc) rnk FROM hr.employees QUALIFY rnk <= 5 order by rnk;
-- 7. Employees who joined on 2004
SELECT * FROM hr.employees WHERE cast(hire_date as string) like '%2004%';
-- 8. Employees whose name starts with 'a'
SELECT first_name FROM hr.employees WHERE first_name like 'A%';
-- 9. department with highest employee count
SELECT department_id, count(*) cnt, row_number() over (order by count(*) desc) rn FROM hr.employees
group by department_id
qualify rn = 1;
-- 10. highest salary in each department
SELECT department_id, salary, dense_rank() over (partition by department_id order by salary desc) rnk
FROM hr.employees
qualify rnk = 1;

-- 11. update employee salary with 10% 
-- update hr.employees set salary = salary*0.01;
-- 12. youngest employee of the company
SELECT first_name,hire_date, dense_rank() over (order by hire_date desc) rnk FROM hr.employees QUALIFY rnk = 1;

SELECT first_name, hire_date FROM hr.employees ORDER BY hire_date DESC LIMIT 1; -- Worst and Inaccurate method.(Inaccurate because it will give ove record even though multiple records)

-- 13. Fetch first and last records from the table.
SELECT *, row_number() over (order by employee_id asc) rnk from hr.employees qualify rnk = 1
union distinct
select *, row_number() over (order by employee_id desc) rnk from hr.employees qualify rnk = 1;

(SELECT * FROM hr.employees ORDER BY employee_id DESC LIMIT 1)
UNION DISTINCT
(SELECT * FROM hr.employees ORDER BY employee_id ASC LIMIT 1);

-- 14. distinct department ids from the employees table
SELECT COUNT(DISTINCT department_id) FROM hr.employees;

-- 15. department with lowest average salary
SELECT department_id, AVG(salary) avg_sal, DENSE_RANK() OVER (ORDER BY AVG(salary) ASC) rnk
FROM hr.employees
GROUP BY department_id
QUALIFY rnk = 1;

-- 16. employees with more than 19 years in a company
select * from hr.employees where date_diff(current_date(),hire_date,year) > 19;
-- 17. managers who doesnt have any employees under him.
select m.employee_id, m.department_id from hr.employees 
select * from hr.employees where employee_id in (select manager_id from hr.employees)

-- 18. department with lowest average salary
select department_id, avg(salary) avg_sal, dense_rank() over (order by avg(salary)) rnk
from hr.employees
group by 1
qualify rnk=1
order by 3;

-- 19. employees working more than 20 years in a company
select first_name, hire_date from hr.employees
where hire_date < date_sub(current_date(),interval 20 year);

-- 20. return current month's name
select format_date('%B',current_date());

-- 21. employees dont have any people under him.
select employee_id,first_name from hr.employees where employee_id not in (select manager_id from hr.employees);

-- 22. write a query to check the table is empty or not
select case when exists(select 1 from hr.employees) then 'Not empty' else 'Empty' end tbl_chk;

-- 23. second highest salary of each department
select department_id, salary, dense_rank() over (partition by department_id order by salary desc) rnk from hr.employees
qualify rnk = 2;

-- 24. employees getting salary multiple of 10000
select salary from hr.employees where mod(salary,10000) = 0;

-- 25. employees who works in both 101,102 departments
select employee_id, count(*) from hr.employees
where department_id in (101,102)
group by employee_id
having count(*) > 1;

-- 26. employees with same salary
select first_name,salary, count(1) over (partition by salary) cnt
from hr.employees
qualify cnt>1
order by cnt;

-- 27. employees hired in last 6 months
select first_name, hire_date from hr.employees where hire_date > date_sub(current_date(), interval 6 month);

-- 28. employees who joined on same month and year as manager.
select e.employee_id,e.first_name,e.hire_date
from hr.employees e join hr.employees m
on e.manager_id = m.employee_id
and format_date('%m%Y',e.hire_date) = format_date('%m%Y',m.hire_date);

-- 29. number of employees whose first letter and last letter is same.
select count(*) from hr.employees
where substr(lower(first_name),1,1) = substr(first_name,-1,1);

-- 30. employees who is getting more than their manager salary
select e.first_name, e.salary, m.salary man_sal 
from hr.employees e join hr.employees m
on e.manager_id = m.employee_id
and e.salary > m.salary;

-- 31. list of employees whos department has less than 3 employees
select e.employee_id, e.department_id, count(*) over (partition by department_id) cnt
from `hr.employees` e
qualify cnt <= 3;

-- 32. employees with same first names
select employee_id, first_name, count(*) over (partition by first_name) cnt
from hr.employees
qualify cnt > 1
order by first_name;

-- 33. list of employees who earns more than avg of their departments.
select first_name, salary , department_id, avg(salary) over (partition by department_id) avg_sal
from hr.employees
qualify avg_sal < salary;
-- using subquery
select * from hr.employees t1 where salary > (select avg(salary) from hr.employees t2 where t2.department_id = t1.department_id);

-- 34. list of employees whose salary in top 10%
select first_name, salary ,percentile_cont(salary,0.9) over () perc from hr.employees
qualify salary >= perc;

-- 35. percentage of employees in each department
select department_id, count(*) * (select distinct 100/count(*) over () each_emp_share from hr.employees) share from hr.employees
group by department_id;

