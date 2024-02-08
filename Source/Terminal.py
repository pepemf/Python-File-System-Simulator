# Path: Source/Main/Terminal.py
from DirectoryClass import Directory
import Binaries
from User import User


rootdir = Directory("/")
user_input = ""	


def bootProcess(rootdir: Directory):
    # Boot the system

    dirBootList = ["bin", "etc", "home", "lib", "mnt", "opt", "usr", "var"]
    homebootList = ["documents", "downloads", "music", "pictures", "videos"]
    binBootList = ["cd", "ls", "mkdir", "touch", "whoami"]

    print("Booting the system...")
    print("System booted successfully.")
    __newuser = input("Enter your username: ")
    Binaries.clear()
    user = User(__newuser, rootdir)

    # Create root directories and files
    for i in dirBootList:
        rootdir.addDirectory(i)
    
    # Create bin files
    for i in binBootList:
        rootdir.subdirectories[0].addFile(i)
        

    rootdir.subdirectories[2].addDirectory(__newuser)
    homefile = rootdir.subdirectories[2].showDirectories()[0]

    # Create home directories
    for i in homebootList:
        homefile.addDirectory(i)
    

    print(f"Welcome to the terminal {__newuser}.")
    print("Type 'help' to see the list of commands.")

    return user

def getpath(user: User):
    
    path = user.currentPath.name
    parent = user.currentPath.parent

    while parent is not None:

        path = parent.name + "/" + path
        parent = parent.parent
    return path

# Initializing Terminal

user = bootProcess(rootdir)

while user_input != "exit":
    user_input = input(f"{user.name}$ {getpath(user)} > ")
    Binaries.switch(user_input, user)


