import numpy as np

# Example dataset: Total monthly sales
sales_data = np.array([2500, 2700, 3000, 2800, 3500, 4000])

# Mean
mean_sales = np.mean(sales_data)
print(f"📊 Mean Sales: {mean_sales:.2f}")

# Median
median_sales = np.median(sales_data)
print(f"📊 Median Sales: {median_sales:.2f}")

# Standard Deviation
std_sales = np.std(sales_data)
print(f"📊 Standard Deviation: {std_sales:.2f}")

# Other useful NumPy functions (optional additions you may have learned)
print(f"🔢 Minimum Sale: {np.min(sales_data)}")
print(f"🔢 Maximum Sale: {np.max(sales_data)}")
print(f"🔢 Sales Range: {np.ptp(sales_data)}")  # Peak to Peak (max - min)
