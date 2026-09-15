# Task 2: A Line Plot with Pandas

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# connect to the SQLite database
conn = sqlite3.connect('../db/lesson.db')

# SQL to create a DataFrame with the order_id and the total_price for each order. 
query = """
    SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id;
"""

# Load results directly into a DataFrame
order_results = pd.read_sql_query(query, conn)
conn.close()

# look to the dataframe
print(order_results.head(5))

# Add a "cumulative" column to the DataFrame. 
def cumulative(row):
   totals_above = order_results['total_price'][0:row.name+1]
   return totals_above.sum()

order_results['cumulative'] = order_results.apply(cumulative, axis=1)

# look to the dataframe with the new cumulative column
print(order_results.head(5))

# a line plot of cumulative revenue vs. order_id.
ax = order_results.plot(
    x='order_id',
    y='cumulative',
    kind='line',
    color='royalblue',
    legend=False
)

# Add titles, labels, and layout adjustments
plt.title('Cumulative Revenue by Order')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue ($)')
plt.tight_layout()

# show plot
plt.show()