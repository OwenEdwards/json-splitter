# json-splitter-gui and json-splitter-add-instanceid-to-note

A simple command line tool for splitting large JSON files into smaller files. Python 3+ is required for this script to work. Modified to add the AMP InstanceID to the end of the Note field for each instance in the input file, and renamed to reflect this.

## Table of Contents

- [json-splitter-add-instanceid-to-note](#json-splitter-add-instanceid-to-note)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Support](#support)

## json-splitter-gui

### Installation

 I created a version that's a Windows executable which allows you to select whether you want to copy the Instance ID to the Note field or not. Windows will try to stop you from running an executable that you download via a link like this, with a dialog saying "Windows protected your PC", but if you click "More info" in that dialog, it shows you a "Run anyway" button.

[json-splitter-gui.exe](https://levelaccess-my.sharepoint.com/:u:/p/owen_edwards/EZJFhzxMy_BBqD3X_z_DHJYBVxPNUbT5IYE1-OnCFr_bDw?e=IWecw3)

### Usage

You can't drag-and-drop a file into the app, but if you view the file you want to split in Windows Explorer and copy it (Ctrl+C), you can go to the Filename field in the app and just paste (Ctrl+V) the filename in there. The split files will show up in the same folder as the original file.


## json-splitter-add-instance-id

### Installation

This script requires Python to be installed on the local machine. Please visit [Python.org](https://www.python.org/) to install or type `python3 --version` to verify it is already installed. On Windows, open a command prompt and type `python3 --version` - if Python isn't already installed, the Microsoft Store app will open and give you the option to install it.

Once Python is installed, download json-splitter-add-instanceid-to-note.py.

### Usage

Place a JSON file within the same directory as the script. The JSON file must be an Array of Objects or Multidimensional Array.

Navigate to the directory where the script exists and begin by typing `python3 json-splitter-add-instanceid-to-note.py`

Enter the name of the JSON file (include the extension) when prompted, then enter the maximum number of MB for each file.

The script will complete and equally split the JSON file into the appropriate number of files to stay under the maximum size.

## Support

(TBD)