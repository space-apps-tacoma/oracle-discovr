# Extract data from gz files

# Import package
import gzip
import os

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
