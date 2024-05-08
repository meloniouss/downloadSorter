# Download Sorter

Download Sorter is a Python script designed to organize files into specified folders based on file extensions or custom file names. This script provides a convenient way to keep your downloads folder or any other directory organized and clutter-free.

## Features

- **File Sorting**: Automatically sorts downloaded files into designated folders based on predefined rules.
- **Configuration Settings**: Allows customization of sorting rules using a configuration file (`config.txt`).
- **Support for Extensions and Custom Names**: Supports sorting files based on both file extensions and custom file names.
- **Cross-Platform Compatibility**: Developed in Python, making it compatible with Windows, macOS, and Linux operating systems.

## Getting Started

  NOTE: If you'd like to run it on startup, you can add modify the file path of the provided Batch file and have it run as a service on startup.

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/meloniouss/download-sorter.git
```

2. Navigate to the project directory:

```
cd download-sorter
```

### Usage

1. Open the `config.txt` file and specify the sorting rules in the following format:

```
# Sorting rules for file extensions
.pdf: PDFs
.jpg,.png: Images
.docx,.txt: Documents

# Sorting rules for custom file names
CustomName1: CustomFolder1
CustomName2: CustomFolder2
```

2. Run the script by executing the following command:

```
python main.py
```

3. Follow the prompts to provide the file path and initiate the sorting process.

## Work in Progress

- GUI: Working on adding a graphical user interace to make adding paths more intuitive.
- Multiple instances: Working on making so the script can work in multiple directories with varying sorting configurations.

## Contributing

Contributions are welcome! Please feel free to fork the repository, make changes, and submit a pull request, if you have anything you'd like to add.

## License

This project is licensed under the [MIT License](LICENSE).
