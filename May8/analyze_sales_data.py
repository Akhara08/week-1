import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def create_dummy_csv(filename='sales_data.csv'):
    # Create dummy sales data
    data = {
        'Date': pd.date_range(start='2024-01-01', periods=12, freq='M'),
        'Region': ['North', 'South', 'East', 'West'] * 3,
        'SalesPerson': ['Alice', 'Bob', 'Charlie', 'Diana'] * 3,
        'Product': ['Laptop', 'Tablet', 'Phone'] * 4,
        'UnitsSold': np.random.randint(10, 100, size=12),
        'UnitPrice': np.random.uniform(200, 1500, size=12).round(2)
    }
    df = pd.DataFrame(data)
    df['TotalSales'] = (df['UnitsSold'] * df['UnitPrice']).round(2)
    df.to_csv(filename, index=False)
    print(f"Dummy CSV '{filename}' created successfully!")

def analyze_sales_data(filename='sales_data.csv'):
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError("CSV file not found.")

        # Load CSV
        df = pd.read_csv(filename, parse_dates=['Date'])

        print("\n🔍 First 5 rows of data:")
        print(df.head())

        print("\n📊 Data Summary:")
        print(df.describe())

        print("\n📅 Date Range:")
        print(f"{df['Date'].min()} to {df['Date'].max()}")

        print("\n📈 Total Sales by Region:")
        print(df.groupby('Region')['TotalSales'].sum().sort_values(ascending=False))

        print("\n👩‍💼 Top Performing SalesPerson:")
        print(df.groupby('SalesPerson')['TotalSales'].sum().sort_values(ascending=False))

        print("\n🧮 Unique Products Sold:")
        print(df['Product'].unique())

        print("\n📅 Filter: Sales After March 2024")
        print(df[df['Date'] > '2024-03-31'])

        print("\n🔢 Adding Sales Tax (18%) Column:")
        df['SalesWithTax'] = (df['TotalSales'] * 1.18).round(2)
        print(df[['TotalSales', 'SalesWithTax']].head())

        # Plotting
        try:
            region_sales = df.groupby('Region')['TotalSales'].sum()
            region_sales.plot(kind='bar', title='Total Sales by Region', color='skyblue')
            plt.xlabel('Region')
            plt.ylabel('Total Sales')
            plt.tight_layout()
            plt.grid(axis='y', linestyle='--', alpha=0.6)
            plt.show()
        except Exception as e:
            print(f"Plotting error: {e}")

        # NumPy Statistics
        try:
            sales_array = df['TotalSales'].to_numpy()
            print("\n📉 NumPy Statistics:")
            print(f"Mean: {np.mean(sales_array):.2f}")
            print(f"Median: {np.median(sales_array):.2f}")
            print(f"Standard Deviation: {np.std(sales_array):.2f}")
        except Exception as e:
            print(f"NumPy calculation error: {e}")

    except Exception as e:
        print(f"Error: {e}")

# Main
create_dummy_csv()
analyze_sales_data()
