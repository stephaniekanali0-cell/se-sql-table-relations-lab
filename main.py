# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
#Return the first and last names and the job titles

df_boston = pd.read_sql("""SELECT firstName,lastName FROM employees INNER JOIN offices ON employees.officeCode = offices.officeCode WHERE offices.city = 'Boston';""",conn)

# STEP 2
# Replace None with your code
#'Ghost' location. Offices with zero employees
df_zero_emp = pd.read_sql("""SELECT offices.officecode, COUNT(employeeNumber) AS employee_count FROM offices LEFT JOIN employees ON offices.officecode = employees.officecode GROUP BY offices.officecode HAVING employee_count = 0;""", conn)

# STEP 3
# Replace None with your code
#Employees f.name,l.name, city, state, order-by f.name then l.name
df_employee = pd.read_sql("""SELECT firstName, lastName, city, state FROM employees LEFT JOIN offices ON employees.officeCode = offices.officeCode ORDER BY firstName, lastName""",conn)

# STEP 4
# Replace None with your code
# Return all the customer's contact info(f.name, l.name, phone number, salerep )
df_contacts = pd.read_sql("""SELECT contactfirstName, contactlastName, phone, salesRepEmployeeNumber FROM customers WHERE customerNumber NOT IN (SELECT customerNumber FROM orders) ORDER BY contactlastName ASC """,conn)

# STEP 5
# Replace None with your code
# Report of all the customer contacts
df_payment = pd.read_sql("""SELECT contactfirstName, contactlastName, amount, paymentdate FROM customers INNER JOIN payments ON customers.customerNumber = payments.customerNumber ORDER BY CAST(amount AS REAL) DESC""",conn)

# STEP 6
# Replace None with your code
# 4 individuals with loyal service
df_credit = pd.read_sql("""SELECT employees.employeeNumber, firstName, lastName, COUNT(customers.customerNumber) AS customer_count FROM employees INNER JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber GROUP BY employees.employeeNumber, firstName, lastName HAVING AVG(customers.creditLimit) > 90000 ORDER BY customer_count DESC""",conn)

# STEP 7
# Replace None with your code
# Product name and count the number of orders.
df_product_sold = pd.read_sql("""SELECT productName, COUNT(DISTINCT orderdetails.orderNumber) AS numorders, SUM(quantityOrdered) AS totalunits FROM products INNER JOIN orderdetails ON products.productCode = orderdetails.productCode GROUP BY productName ORDER BY totalunits DESC""",conn)

# STEP 8
# Replace None with your code
#Product name, code, total number of customers
df_total_customers = pd.read_sql("""SELECT productName, products.productCode, COUNT(DISTINCT orders.customerNumber) AS numpurchasers FROM products INNER JOIN orderdetails ON products.productCode = orderdetails.productCode INNER JOIN orders ON orderdetails.orderNumber = orders.orderNumber GROUP BY productName, products.productCode ORDER BY numpurchasers DESC """,conn)

# STEP 9
# Replace None with your code
# Return count of customers
df_customers = pd.read_sql("""SELECT offices.officeCode, offices.city, COUNT(customers.customerNumber) AS n_customers FROM offices INNER JOIN employees ON offices.officecode = employees.officecode INNER JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber GROUP BY offices.officecode, offices.city""",conn)

# STEP 10
# Replace None with your code
# employee number, first name, last name, city of office and office code 
df_under_20 = pd.read_sql("""SELECT DISTINCT employees.employeeNumber, employees.firstName, employees.lastName, offices.city, offices.officeCode FROM orderdetails INNER JOIN orders ON orderdetails.orderNumber = orders.orderNumber INNER JOIN customers ON orders.customerNumber = customers.customerNumber INNER JOIN employees ON customers.salesRepEmployeeNumber = employees.employeeNumber INNER JOIN offices ON employees.officeCode = offices.officeCode WHERE orderdetails.productCode IN(SELECT orderdetails.productCode FROM orderdetails INNER JOIN orders ON orderdetails.orderNumber = orders.orderNumber GROUP BY orderdetails.productCode HAVING COUNT(DISTINCT orders.customerNumber) < 20) ORDER BY employees.lastName""",conn)

conn.close()