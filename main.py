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

df_boston = pd.read_sql("""SELECT firstName,lastName,jobTitle FROM employees;""",conn)

# STEP 2
# Replace None with your code
#'Ghost' location. Offices with zero employees
df_zero_emp = pd.read_sql("""SELECT offices.officecode, COUNT(employeeNumber) AS employee_count FROM offices LEFT JOIN employees ON offices.officecode = employees.officecode GROUP BY offices.officecode HAVING employee_count = 0;""", conn)

# STEP 3
# Replace None with your code
#Employees f.name,l.name, city, state, order-by f.name then l.name
df_employee = pd.read_sql("""SELECT firstName, lastName, city, state FROM employees, offices ORDER BY firstName, lastName""",conn)

# STEP 4
# Replace None with your code
# Return all the customer's contact info(f.name, l.name, phone number, salerep )
df_contacts = pd.read_sql("""SELECT firstName, lastName, phone, salesRepEmployeeNumber WHERE customerNumber NOT IN (SELECT customerNumber, FROM orders ORDER BY lastName DESC) FROM customers""",conn)

# STEP 5
# Replace None with your code
df_payment = None

# STEP 6
# Replace None with your code
df_credit = None

# STEP 7
# Replace None with your code
df_product_sold = None

# STEP 8
# Replace None with your code
df_total_customers = None

# STEP 9
# Replace None with your code
df_customers = None

# STEP 10
# Replace None with your code
df_under_20 = None

conn.close()