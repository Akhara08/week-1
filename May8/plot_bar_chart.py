import matplotlib.pyplot as plt

# Dummy sales data
months = ['January', 'February', 'March', 'April', 'May', 'June']
sales = [2500, 2700, 3000, 2800, 3500, 4000]

# Create the bar chart
plt.figure(figsize=(8, 5))                            # Set figure size
plt.bar(months, sales, color='skyblue', edgecolor='black')  # Bar chart with color and edge
plt.title('Monthly Sales')                            # Add a title
plt.xlabel('Month')                                   # X-axis label
plt.ylabel('Sales ($)')                               # Y-axis label
plt.grid(axis='y', linestyle='--', alpha=0.6)         # Add horizontal grid lines
plt.xticks(rotation=45)                               # Rotate x-axis labels for readability
plt.tight_layout()                                    # Adjust layout to prevent overlap
plt.show()                                            # Display the chart
