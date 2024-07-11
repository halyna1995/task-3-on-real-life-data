import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_unique_id_distribution(df):
    """Plot the distribution of unique IDs with their frequency on a histogram."""
    counts = df['unique_id'].value_counts()
    
    plt.figure(figsize=(12, 8))
    plt.hist(counts, bins=50, color='blue', log=True)  # Log scale
    plt.title('Histogram of Unique ID Frequencies', fontsize=20)
    plt.xlabel('Frequency of Unique IDs', fontsize=15)
    plt.ylabel('Number of Unique IDs (Log Scale)', fontsize=15)
    plt.grid(True)
    plt.show()

def analyze_uniqueness(df):
    """Analyze and report on the uniqueness of the 'unique_id'."""
    counts = df['unique_id'].value_counts()
    max_count = counts.max()
    if max_count > 1:
        print(f"The maximum count for a single unique_id is {max_count}, which indicates duplicates.")
    else:
        print("Each 'unique_id' is unique across the dataset.")

def main():
    folder_path = 'G:/Lysunochka/work and coaching from marielle obells/task 2/marielle correction resume+motivation letter/new/phd tue/Dirk tue/task 3 on real-life data from the project/prepared_data/prepared_data'
    all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    df_list = []

    if not all_files:
        print("No CSV files found in the specified directory.")
        return

    for file in all_files:
        file_path = os.path.join(folder_path, file)
        if os.stat(file_path).st_size == 0:  # Check if file is empty
            print(f"Skipping empty file: {file}")
            continue

        df_temp = pd.read_csv(file_path)
        df_temp['Código'] = df_temp['Código'].astype(str).str.strip()
        df_temp['N/S'] = df_temp['N/S'].astype(str).str.strip()
        df_temp['unique_id'] = df_temp['Código'] + '-' + df_temp['N/S']
        df_list.append(df_temp)

    if not df_list:
        print("All files were empty or missing required columns. No data to process.")
        return

    df = pd.concat(df_list, ignore_index=True)
    
    df.dropna(subset=['unique_id'], inplace=True)  # Handle missing values before analysis

    analyze_uniqueness(df)
    plot_unique_id_distribution(df)

if __name__ == "__main__":
    main()
