import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

def custom_plot(df, folder, filename, title, xlabel, ylabel, figsize=(10, 6), fontsize=12, xlabelsize=10, ylabelsize=10):
    # Create the folder if it does not exist
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    plt.figure(figsize=figsize)
    counts = df['unique_id'].value_counts()
    plt.bar(counts.index, counts.values)
    plt.title(title, fontsize=fontsize)
    plt.xlabel(xlabel, fontsize=xlabelsize)
    plt.ylabel(ylabel, fontsize=ylabelsize)
    plt.yscale('log')
    plt.savefig(os.path.join(folder, filename))
    plt.show()
    plt.close()

# The path to the file folder
folder_path = 'G:/Lysunochka/work and coaching from marielle obells/task 2/marielle correction resume+motivation letter/new/phd tue/Dirk tue/task 3 on real-life data from the project/prepared_data/prepared_data'

# Loading all CSV files into a DataFrame list
all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
df_list = [pd.read_csv(os.path.join(folder_path, file)) for file in all_files]

# Combining all DataFrames into one
df = pd.concat(df_list, ignore_index=True)

# Check for 'Código' and 'N/S' columns
if 'Código' in df.columns and 'N/S' in df.columns:
    df['Código'] = df['Código'].astype(str)
    df['N/S'] = df['N/S'].astype(str)
    df['unique_id'] = df['Código'] + '-' + df['N/S']
else:
    print("Columns 'Código' or 'N/S' are missing from the data")

# Extract NaN values ​​before parsing
df_clean = df.dropna(subset=['unique_id'])

# Saving cleaned data to JSON
json_path = os.path.join(folder_path, 'clean_data.json')
df_clean.to_json(json_path, orient='records', lines=True)

# Reading data from JSON
df_clean = pd.read_json(json_path, lines=True)

# Call the rendering function
plot_folder = 'plots'  # Changed to the correct path
custom_plot(df_clean, plot_folder, 'unique_id_distribution.png', 'Distribution of unique identifiers', 'Unique ID', 'Number of records', fontsize=20, xlabelsize=20, ylabelsize=20)
