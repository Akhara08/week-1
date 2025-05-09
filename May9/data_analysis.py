import pandas as pd
import matplotlib.pyplot as plt
import os

def load_csv(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("File does not exist.")
        df = pd.read_csv(file_path)
        print("CSV file loaded successfully.\n")
        print("First few rows of the dataset:\n", df.head())
        return df
    except FileNotFoundError as e:
        print("Error:", e)
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
    except pd.errors.ParserError:
        print("Error: Failed to parse the CSV. Check formatting.")
    except Exception as e:
        print("An unexpected error occurred:", e)

def process_data(df):
    try:
        if 'Category' not in df.columns or 'Value' not in df.columns:
            raise ValueError("Required columns 'Category' and 'Value' not found.")
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
        df = df.dropna(subset=['Value'])
        grouped = df.groupby('Category')['Value'].sum().reset_index()
        return grouped
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred during processing:", e)

def plot_data(grouped_data):
    try:
        plt.figure(figsize=(10, 6))
        plt.bar(grouped_data['Category'], grouped_data['Value'], color='skyblue')
        plt.xlabel('Category')
        plt.ylabel('Total Value')
        plt.title('Total Value by Category')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print("Error while plotting:", e)

def main():
    file_path = input("Enter the CSV file path (e.g., data.csv): ")
    df = load_csv(file_path)
    if df is not None:
        grouped_data = process_data(df)
        if grouped_data is not None:
            print("\nProcessed Data:\n", grouped_data)
            plot_data(grouped_data)

if __name__ == "__main__":
    main()

