import os
import pandas as pd

def combine_csv_files(folder_path, output_file='combined_data.csv'):
    # List to hold data from all CSV files
    combined_data = []
    
    # Print the folder contents
    print(f"Scanning folder: {folder_path}")
    
    # Iterate through all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):  # Only consider CSV files
            file_path = os.path.join(folder_path, file_name)
            
            print(f"Processing file: {file_name}")
            
            try:
                # Read the CSV file
                csv_data = pd.read_csv(file_path)
                
                # Check if the CSV file is not empty
                if not csv_data.empty:
                    combined_data.append(csv_data)
                else:
                    print(f"Warning: CSV file '{file_name}' is empty.")
            
            except Exception as e:
                print(f"Error reading file {file_name}: {e}")
    
    # Check if any data was collected
    if not combined_data:
        print("No data was found to combine.")
        return
    
    # Concatenate all the data into a single DataFrame
    combined_df = pd.concat(combined_data, ignore_index=True)
    
    # Save the combined DataFrame to a new CSV file
    combined_df.to_csv(output_file, index=False)
    
    print(f"Data from all CSV files in {folder_path} has been combined into {output_file}")

# Example usage
folder_path = r"C:\Users\LENOVO\OneDrive\Desktop\data\Panel Lights"  # Replace with your folder path
combine_csv_files(folder_path)
