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
SELECT department_id, AVG(salary) avg_sal, DENSE_RANK() OVER (PARTITION BY department_id ORDER BY AVG(salary)) rnk
FROM hr.employees
GROUP BY department_id
QUALIFY rnk = 1;

