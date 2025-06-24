import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('sales_data.csv')

# Total revenue
df['Revenue'] = df['Quantity'] * df['Price']

# Group by product
product_revenue = df.groupby('Product')['Revenue'].sum()

# Show result
print("Total Revenue per Product:")
print(product_revenue)

# Plot
product_revenue.plot(kind='bar', title='Revenue by Product', color='skyblue')
plt.ylabel('Revenue in Rs.')
plt.savefig('output_chart.png')
plt.show()
