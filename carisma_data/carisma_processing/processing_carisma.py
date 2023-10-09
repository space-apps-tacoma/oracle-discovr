# Process the carisma data from text to csv files

# Import packages
import os
import pandas as pd

# File paths
file_path = "C:\\Users\\socce\\OneDrive\\Documents\\Space Apps 2023\\2016_extracted"

# Initialize data dictionary
data_dict = {}

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
            location = split_header[0]
              
            lines = file.readlines()
            timestamp = ""

            for line in lines:
                print('\n' in line, "checking newline char")

                if line.startswith('201'):
                    
                    timestamp = line[0:12]

                    # Check if the outermost key exists, create it if it doesn't
                    if timestamp not in data_dict:
                        data_dict[timestamp] = {}

                    # Check if the inner dictionary key 'x' exists, create it if it doesn't
                    if 'x' not in data_dict[timestamp]:
                        data_dict[timestamp]['x'] = []

                    # Check if the inner dictionary key 'y' exists, create it if it doesn't
                    if 'y' not in data_dict[timestamp]:
                        data_dict[timestamp]['y'] = []

                    # Check if the inner dictionary key 'x' exists, create it if it doesn't
                    if 'z' not in data_dict[timestamp]:
                        data_dict[timestamp]['z'] = []

                else:
                    coordinates = line.split()

                    if len(coordinates) == 3:
                        data_dict[timestamp]['x'].append(coordinates[0])
                        data_dict[timestamp]['y'].append(coordinates[1])
                        data_dict[timestamp]['z'].append(coordinates[2])

                
print(pd.DataFrame(data_dict).head())




"""
# Initialize empty lists to store the data
timestamps = []
coordinates = []

# Open the file for reading
with open("data.txt", "r") as file:
    lines = file.readlines()

# Initialize variables to hold the current timestamp and coordinates
current_timestamp = None
current_coordinates = []

# Iterate through the lines in the file
for line in lines:
    # Strip leading and trailing whitespace from each line
    line = line.strip()

    # Check if the line is empty
    if not line:
        continue

    # Check if the line starts with a timestamp
    if line.startswith("20"):
        # If a new timestamp is encountered, store the previous one and its coordinates
        if current_timestamp is not None:
            timestamps.append(current_timestamp)
            coordinates.append(current_coordinates)
        # Parse the new timestamp
        current_timestamp = line.split()[0]
        current_coordinates = []
    else:
        # Parse the coordinates and append them to the current_coordinates list
        parts = line.split()
        coordinates.extend([float(part) for part in parts])

# Append the last timestamp and its coordinates
if current_timestamp is not None:
    timestamps.append(current_timestamp)
    coordinates.append(current_coordinates)

# Print the extracted data (optional)
for i in range(len(timestamps)):
    print("Timestamp:", timestamps[i])
    print("Coordinates:", coordinates[i])
    print()

# Now, you have the timestamps in the 'timestamps' list and the corresponding coordinates in the 'coordinates' list.
"""
