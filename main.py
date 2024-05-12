import os
import shutil
import re
import threading

extension_destinations = {}
customFile_destinations = {}
regex_destinations = {}
paths = []


def create_destination_dirs(sort_path_, destinations):  # creating destination directories if they don't exist
    for destination in set(destinations.values()):
        destination_directory = os.path.join(sort_path_, destination)
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)


def parse_config_file():
    with open("config.txt", "r") as cfgFile:
        for line in cfgFile:
            line = line.strip()
            if not line.startswith("#") and "=" in line:
                path_line = line.split("=")[1]
                paths.extend(path_line.split(","))
                break
        for line in cfgFile:
            line = line.strip()
            if line.startswith("#"):
                continue
            else:
                extensions, folder = line.strip().split(":")
                for extension in extensions.split(","):
                    if extension.startswith("."):
                        extension_destinations[extension.strip()] = folder.strip()
                    elif extension.startswith("pm_"):
                        extension = extension[3:]
                        regex_destinations[extension.strip()] = folder.strip()
                    elif "pm_" in extension:
                        regex_destinations[extension.strip()] = folder.strip()
                    else:
                        customFile_destinations[extension.strip()] = folder.strip()


def sort_path(path_):

    files = os.listdir(path_)
    create_destination_dirs(path_, extension_destinations)
    create_destination_dirs(path_, customFile_destinations)
    create_destination_dirs(path_, regex_destinations)
    moved_files = set()
    for file in files:  # here we are doing the same loop but using pattern matching
        if file in moved_files:
            continue
        file_extension = os.path.splitext(file)[1]
        for regex_pattern, folder in regex_destinations.items():
            if re.match(regex_pattern, file[:file.rfind(".")]):  # finds the last occurrence of . character, which coincides with the start of the extension
                destination_dir = os.path.join(path_, folder)
                destination_file_path = os.path.join(destination_dir, file)
                if not os.path.exists(destination_file_path):
                    shutil.move(os.path.join(path_, file), destination_file_path)
                    moved_files.add(file)
                break
    for file in files:  # now, here we check for custom file names
        if file in moved_files:
            continue
        file_extension = os.path.splitext(file)[1]
        for custom_name, folder in customFile_destinations.items():
            if custom_name in file:
                destination_dir = os.path.join(path_, folder)
                destination_file_path = os.path.join(destination_dir, file)
                if not os.path.exists(destination_file_path):
                    shutil.move(os.path.join(path_, file), destination_file_path)
                    moved_files.add(file)
                break
    for file in files:  # here we are moving files based on their extensions
        if file in moved_files:
            continue
        file_extension = os.path.splitext(file)[1]
        if file_extension in extension_destinations:
            destination_dir = os.path.join(path_, extension_destinations[file_extension])
            destination_file_path = os.path.join(destination_dir, file)
            if not os.path.exists(destination_file_path):
                shutil.move(os.path.join(path_, file), destination_file_path)
                moved_files.add(file)


parse_config_file()
threads = []
for path in paths:
    thread = threading.Thread(target=sort_path, args=(path,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

