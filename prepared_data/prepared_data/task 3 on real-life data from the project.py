# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:57:44 2024

@author: shmot
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:54:40 2024

@author: shmot
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import json

def custom_plot(df, folder, filename, title, xlabel, ylabel, figsize=(10, 6), fontsize=12, xlabelsize=10, ylabelsize=10):
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

def plot_unique_id_distribution(df, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    counts = df['unique_id'].value_counts()
    plt.figure(figsize=(12, 8))
    plt.hist(counts, bins=50, color='blue', log=True)
    plt.title('Histogram of Unique ID Frequencies', fontsize=20)
    plt.xlabel('Frequency of Unique IDs', fontsize=15)
    plt.ylabel('Number of Unique IDs (Log Scale)', fontsize=15)
    plt.grid(True)
    plt.savefig(os.path.join(folder, 'histogram_unique_id.png'))
    plt.show()

def analyze_uniqueness(df):
    counts = df['unique_id'].value_counts()
    max_count = counts.max()
    if max_count > 1:
        print(f"The maximum count for a single unique_id is {max_count}, which indicates duplicates.")
    else:
        print("Each 'unique_id' is unique across the dataset.")

def main():
    folder_path = 'G:/Lysunochka/work and coaching from marielle obells/task 2/marielle correction resume+motivation letter/new/phd tue/Dirk tue/task 3 on real-life data from the project/prepared_data/prepared_data'
    output_folder = 'output'  # Folder for outputs including plots and JSON files
    all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    df_list = []

    if not all_files:
        print("No CSV files found in the specified directory.")
        return

    for file in all_files:
        file_path = os.path.join(folder_path, file)
        if os.stat(file_path).st_size == 0:
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
    df.dropna(subset=['unique_id'], inplace=True)

    # Save to JSON
    json_path = os.path.join(output_folder, 'cleaned_data.json')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    df.to_json(json_path, orient='records', lines=True)

    analyze_uniqueness(df)
    custom_plot(df, output_folder, 'unique_id_distribution.png', 'Distribution of unique identifiers', 'Unique ID', 'Number of records', fontsize=20, xlabelsize=20, ylabelsize=20)
    plot_unique_id_distribution(df, output_folder)

if __name__ == "__main__":
    main()
