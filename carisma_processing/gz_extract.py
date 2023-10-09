# Extract data from gz files

# Import package
import os
import sys
import gzip
import shutil

"""
# Years of data to extract
years = ['2016', '2017']

# Days of data to extract
days = ['06', '07', '08']

# Root file path to gz files
root_file_path = 'C:/Users/socce/OneDrive/Documents/Space Apps 2023/2017/09/'

# Read data in gz file
for day in days:
    root_day_path = root_file_path + day + '/'

    for filename in os.listdir(root_day_path):
        if filename.endswith('.gz'):
            gz_file_path = os.path.join(root_day_path, filename)

            # Create folder to store extracted data
            extracted_data_folder = root_day_path + day + '_extracted_data/'
            os.makedirs(extracted_data_folder, exist_ok=True)

            # Extract data from Gzip file
            with gzip.open(gz_file_path, 'rb') as gz_file:
                gz_contents = gz_file.read().decode('utf-8')

                # Save extracted data to file
                extracted_data_file = os.path.join(extracted_data_folder, f"{filename}.txt")
                with open(extracted_data_file, 'w', encoding='utf-8') as output_file:
                    output_file.write(gz_contents)
"""
                    
def extract_gzip(file_path, extract_dir):
    try:
        # Create new folder name for extracted data
        extracted_folder_name = file_path[-4:] + '_extracted'
        # Create new folder path for extracted data
        extracted_folder_path = os.path.join(extract_dir, extracted_folder_name)
        os.makedirs(extracted_folder_path, exist_ok=True)  # Create the folder if it doesn't exist
        
        # Loop through each month in year folder
        for month in os.listdir(file_path):
            # Create path for month directory
            month_path = file_path + "\\" + month
            # Loop through each day in month folder
            for day in os.listdir(month_path):
                # Create path for day directory
                day_path = month_path + "\\" + day + "\\"
                # Loop through each file in day folder
                for filename in os.listdir(day_path):
                    
                    # Check if the file is a .gz file
                    if filename.endswith('.gz'):
                        
                        gz_path = os.path.join(day_path, filename)
                        # Open the gzip file for reading
                        with gzip.open(gz_path, 'rb') as gz_file:
                            gz_contents = gz_file.read().decode('utf-8')
                            
                            # Save extracted data to file
                            extracted_data_file = os.path.join(extracted_folder_path, f"{filename}.txt")
                            # Open the destination file for writing
                            with open(extracted_data_file, 'w', encoding='utf-8') as dest_file:
                                dest_file.write(gz_contents)
                            
        
        print(f"Successfully extracted data to '{extracted_folder_path}'")
    except Exception as e:
        print(f"Error extracting '{file_path}': {e}")

if __name__ == "__main__":
    # Check for the correct number of command line arguments
    if len(sys.argv) != 3:
        print("Usage: python extract_gzip.py <file_name> <directory_path>")
        sys.exit(1)

    # Get the file name and directory path from command line arguments
    file_name = sys.argv[1]
    directory_path = sys.argv[2]

    # Check if the file exists
    file_path = os.path.join(directory_path, file_name)
    if not os.path.isdir(file_path):
        print(f"Directory '{file_path}' not found.")
        sys.exit(1)

    # Call the extract_gzip function to extract the contents
    extract_gzip(file_path, directory_path)
