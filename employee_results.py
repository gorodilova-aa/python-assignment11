# Task 1: Plotting with Pandas

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# connect to the SQLite database
conn = sqlite3.connect('db/lesson.db')

# SQL to join the employees table with the orders table with the line_items table with the products table. 
# You then group by employee_id, and you SELECT the last_name and revenue, where revenue is the sum of price * quantity. 
query = """
    SELECT last_name, SUM(price * quantity) AS revenue 
    FROM employees e 
    JOIN orders o ON e.employee_id = o.employee_id 
    JOIN line_items li ON o.order_id = li.order_id 
    JOIN products p ON li.product_id = p.product_id 
    GROUP BY e.employee_id;
"""

# Load results directly into a DataFrame
employee_results = pd.read_sql_query(query, conn)
conn.close()

# look to the dataframe
print(employee_results.head(5))

# bar chart where the x axis is the employee last name and the y axis is the revenue
ax = employee_results.plot(
    x='last_name',
    y='revenue',
    kind='bar',
    color='royalblue',
    legend=False,
    rot=45
)

# Add titles, labels, and layout adjustments
plt.title('Total Revenue by Employee')
plt.xlabel('Employee Last Name')
plt.ylabel('Revenue ($)')
plt.tight_layout()

# show plot
plt.show()