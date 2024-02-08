# Terminal Simulator

## Description
This project simulates a basic terminal environment where users can navigate through directories, create files and directories, edit file contents, and execute various terminal commands.

## Files
### Terminal.py
* This file contains the main funcionality of the terminal simulation
* It initializes the ssystem, creates directories, sets up user environment, and handle the user inputs
* Users can interact with the terminal through commands such as **mkdir**, **ls**, **cd**, **touch**, **nano**, **cat**, **whoami**, and **clear**

### FileClass.py
* Defines the File class which represents files in the terminal environment.
* Users can create, edit, and view the content of files

### DirectoryClass.py
* Defines the Directory class, representing directories in the terminal environment.
* Users can create, delete, and navigate through directories

### Binaries.py
* Contains executable binary funcions for terminal commands.

### Tests.py
* includes unit tests for various functionalities in the project
* Tests cover funcionalities such as creating directories, creating files, changing directories, and user identifications.

## Usage
1. #### Ensure you have python3 installed on your system.
2. #### Clone this repository with the following command:
```bash
git clone https://https://github.com/pepemf/Python-Terminal-Simulator
```
1. #### Inside the cloned directory, start the script by running
```bash
Python Terminal.py
```
1. #### Interact with the Terminal: Once the terminal simulator is running, you can interact with it using various commands. For example:
* To list avaliable commands: **help**
* To create a directory: **mkdir new_directory**
* To list files and directories: **ls**
* To change the current directory: **cd new_directory**
* To create a new file: **touch new_file.txt**
* To edit a file: **nano file.txt**
* To view the content of a file: **cat file.txt**
* To clear the terminal screen: **clear**
* To exit the terminal simulator: **exit**
