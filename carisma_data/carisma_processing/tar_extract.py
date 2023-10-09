# Extract and access tarfile data from CARISMA Magnetometer Network

# Import libraries
import os
import sys
import tarfile

def extract_tar(file_path, extract_dir):
    try:
        # Open the tar file for reading
        with tarfile.open(file_path, 'r') as tar:
            # Extract its contents into the specified directory
            tar.extractall(path=extract_dir)
        print(f"Successfully extracted '{file_path}' to '{extract_dir}'")
    except tarfile.TarError as e:
        print(f"Error extracting '{file_path}': {e}")

if __name__ == "__main__":
    # Check for the correct number of command line arguments
    if len(sys.argv) != 3:
        print("Usage: python extract_tar.py <file_name> <directory_path>")
        sys.exit(1)

    # Get the file name and directory path from command line arguments
    file_name = sys.argv[1]
    directory_path = sys.argv[2]

    # Check if the file exists
    file_path = os.path.join(directory_path, file_name)
    if not os.path.isfile(file_path):
        print(f"File '{file_path}' not found.")
        sys.exit(1)

    # Check if the file is a .tar file
    if not file_name.endswith('.tar'):
        print(f"'{file_path}' is not a .tar file.")
        sys.exit(1)

    # Call the extract_tar function to extract the contents
    extract_tar(file_path, directory_path)
