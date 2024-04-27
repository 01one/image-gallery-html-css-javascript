""" file location
import os
import glob

def find_files_by_extensions(directory, extensions):
    # Navigate to the directory
    os.chdir(directory)
    
    # Search for files with the specified extensions
    files = []
    for ext in extensions:
        files.extend(glob.glob('*.' + ext))
    
    # Return the list of file locations
    return [os.path.abspath(file) for file in files]

# Example usage
directory_path = 'static/images'
extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp']  # List of image extensions
file_locations = find_files_by_extensions(directory_path, extensions)
print("Image files found in directory '{}':".format(directory_path))
for location in file_locations:
    print(location)
"""



# File names

import os
import glob

def find_files_by_extensions(directory, extensions):
    # Navigate to the directory
    os.chdir(directory)
    
    # Search for files with the specified extensions
    files = []
    for ext in extensions:
        files.extend(glob.glob('*.' + ext))
    
    # Return the list of file names
    return files

# Example usage
directory_path = 'static/images'
extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp']  # List of image extensions
file_names = find_files_by_extensions(directory_path, extensions)
print("Image files found in directory '{}':".format(directory_path))
for name in file_names:
    print(name)
