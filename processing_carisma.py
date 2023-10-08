# Process the carisma data from text to csv files

# Import packages
# import pandas as pd
import os

# File paths
file_path = 'carisma_data/2017-09-06/'

# Loop through .txt files
for filename in os.listdir(file_path):
        # Only access .txt files
        if filename.endswith('.txt'):
            # Create a path for this file
            txt_file_path = os.path.join(file_path, filename)

            # Open file for reading
            with open(txt_file_path, 'r') as file:
                  header = file.readline()
                  split_header = header.split()
                  
                  
