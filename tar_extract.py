# Extract and access tarfile data from CARISMA Magnetometer Network

# Import libraries
import tarfile

# Years of tarfile data
years = ['2016', '2017']

# Tarfile location path
root_tar_file_path = '../../OneDrive/Documents/Space Apps 2023/'

# Extract tarfile contents
for year in years:
    with tarfile.open(root_tar_file_path+year+'.tar', 'r') as tar:
        # List the contents of the .tar file
        tar.extractall(path='../../OneDrive/Documents/Space Apps 2023/')
