# json-splitter-add-instanceid-to-note
A simple command line tool for splitting large JSON files into smaller files. Python 3+ is required for this script to work. Modified to add the AMP InstanceID to the end of the Note field for each instance in the input file, and renamed to reflect this.

## Table of Contents

- [json-splitter-add-instanceid-to-note](#json-splitter-add-instanceid-to-note)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Support](#support)

## Installation
This script requires Python to be installed on the local machine. Please visit [Python.org](https://www.python.org/) to install or type `python3 --version` to verify it is already installed.

Once Python is installed, download json-splitter-add-instanceid-to-note.py.

## Usage
Place a JSON file within the same directory as the script. The JSON file must be an Array of Objects or Multidimensional Array.

Navigate to the directory where the script exists and begin by typing `python3 json-splitter-add-instanceid-to-note.py`

Enter the name of the JSON file (include the extension) when prompted, then enter the maximum number of MB for each file.

The script will complete and equally split the JSON file into the appropriate number of files to stay under the maximum size.

## Support
Please (TBD) for support.