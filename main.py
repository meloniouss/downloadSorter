import os
import shutil

extension_destinations = {}
path = ''
with open("config.txt", "r") as cfgFile:

    for line in cfgFile:  # looking for the path in this loop
        line = line.strip()
        if not line.startswith("#") and "=" in line:
            path = line.split("=")[1]
            break
    for line in cfgFile:
        line = line.strip()
        if line.startswith("#"): # here we check whether the line is a comment or not
            continue
        else:
            extensions, folder = line.strip().split(":")
            for extension in extensions.split(","):
                extension_destinations[extension.strip()] = folder.strip()

# prompt the user to enter a file path if it's empty
if path == '':
    path = input(
        "Please enter a file path in the following format: Drive:/Folder/File (...), then press enter to select the "
        "folder you would like to sort.")
    # Write the file path to config.txt
    with open("config.txt", "w") as pathFile:
        pathFile.write("SORTING_PATH=" + path)

# creating destination directories if they don't exist
for destination in set(extension_destinations.values()):
    destination_dir = os.path.join(path, destination)
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

files = os.listdir(path)
for file in files:
    file_extension = os.path.splitext(file)[1]
    if file_extension in extension_destinations:
        destination_dir = os.path.join(path, extension_destinations[file_extension])
        destination_file_path = os.path.join(destination_dir, file)
        if not os.path.exists(destination_file_path):
            shutil.move(os.path.join(path, file), destination_file_path)
