import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Product Name': ['computer', 'sockets', 'laptops', 'pu', 'keyboards', 'chip', 'wires'],
    'Number': [100, 150, 200, 250, 243, 350, 450],
    'Defects': [5, 10, 8, 9, 3, 7, 9],
    'Non-Defects': [95, 140, 192, 234, 89, 98, 95]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Plotting the stacked bar chart
ax = df.plot(x='Product Name', kind='bar', stacked=True,
             y=['Defects', 'Non-Defects'], figsize=(10, 6))

# Set title and labels
plt.title('Defects and Non-Defects by Product')
plt.xlabel('Product Name')
plt.ylabel('Number of Units')

# Add legend
plt.legend(title='status')

# Show the plot
plt.show()
