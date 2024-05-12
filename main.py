import os
import shutil
import re

extension_destinations = {}
customFile_destinations = {}
regex_destinations = {}  # we will use this
path = ''


def create_destination_dirs(sort_path, destinations):  # creating destination directories if they don't exist
    for destination in set(destinations.values()):
        destination_directory = os.path.join(sort_path, destination)
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)


with open("config.txt", "r") as cfgFile:
    for line in cfgFile:  # looking for the path in this loop
        line = line.strip()
        if not line.startswith("#") and "=" in line:
            path = line.split("=")[1]
            break
    for line in cfgFile:
        line = line.strip()
        if line.startswith("#"):  # here we check whether the line is a comment or not
            continue
        else:
            extensions, folder = line.strip().split(":")
            for extension in extensions.split(","):
                if extension.startswith("."):
                    extension_destinations[extension.strip()] = folder.strip()
                elif extension.startswith("pm_"):
                    extension = extension[3:]
                    regex_destinations[extension.strip()] = folder.strip()
                else:
                    customFile_destinations[extension.strip()] = folder.strip()


# prompt the user to enter a file path if it's empty
if path == '':
    path = input(
        "Please enter a file path in the following format: Drive:/Folder/File (...), then press enter to select the "
        "folder you would like to sort.")
    # Write the file path to config.txt
    with open("config.txt", "w") as pathFile:
        pathFile.write("SORTING_PATH=" + path)


files = os.listdir(path)
create_destination_dirs(path, extension_destinations)
create_destination_dirs(path, customFile_destinations)
create_destination_dirs(path, regex_destinations)


#  /////////////////////////////////////////////////////
#  As you can see, we don't use functions here because
#  each iteration through the files is slightly different.
#  /////////////////////////////////////////////////////


for file in files:  # here we are moving files based on their extensions
    file_extension = os.path.splitext(file)[1]
    if file_extension in extension_destinations:
        destination_dir = os.path.join(path, extension_destinations[file_extension])
        destination_file_path = os.path.join(destination_dir, file)
        if not os.path.exists(destination_file_path):
            shutil.move(os.path.join(path, file), destination_file_path)
for file in files:  # now, here we check for custom file names
    file_extension = os.path.splitext(file)[1]
    for custom_name, folder in customFile_destinations.items():
        if custom_name in file:
            destination_dir = os.path.join(path, folder)
            destination_file_path = os.path.join(destination_dir, file)
            if not os.path.exists(destination_file_path):
                shutil.move(os.path.join(path, file), destination_file_path)
            break
for file in files:  # here we are doing the same loop but using pattern matching
    file_extension = os.path.splitext(file)[1]
    for regex_pattern, folder in regex_destinations.items():
        print(re.match(regex_pattern, os.path.splitext(file)[0]))
        if re.match(regex_pattern, os.path.splitext(file)[0]):  # it matches the first element of the tuple (the file
            # name, rather than the file name + the extension)
            destination_dir = os.path.join(path, folder)
            destination_file_path = os.path.join(destination_dir, file)
            if not os.path.exists(destination_file_path):
                shutil.move(os.path.join(path, file), destination_file_path)
            break
