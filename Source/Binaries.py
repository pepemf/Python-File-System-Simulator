from Source.DirectoryClass import Directory
from Source.User import User


def mkdir(currentDirectory: Directory, name) -> bool:
    '''
    Recieves a directory and a name and creates a new directory with the given name in the given directory.

    Parameters:
    currentDirectory: Directory
        The directory in which the new directory will be created.
    name: str
        The name of the new directory.

    Returns:
        bool
            True if the directory was created successfully, False if the directory already exists.
    '''
    
    # It only supports creating a directory in the current directory for now.
    # In the future, it will support creating a directory in the specified path.

    try:
        currentDirectory.addDirectory(name)
        return True
    except FileExistsError:
        raise FileExistsError
        return False


def touch(fileName, currentDirectory: Directory) -> bool:
    '''
    Recieves a directory and a name and creates a new file with the given name in the given directory.

    Parameters:
    currentDirectory: Directory
        The directory in which the new file will be created.
    name: str
        The name of the new file.

    Returns:
        bool
            True if the file was created successfully, False if the file already exists.
    
    '''

    try:
        currentDirectory.addFile(fileName)
        return True
    except FileExistsError:
        raise FileExistsError
        return False

def rm(currentDirectory: Directory, name: str) -> bool:
    '''
    Recieves a directory and a name and removes the file with the given name from the given directory.

    Parameters:
    currentDirectory: Directory
        The directory from which the file will be removed.
    name: str
        The name of the file that will be removed.

    Returns:
        bool
            True if the file was removed successfully, False if the file does not exist.
    '''

    try:
        currentDirectory.removeFile(name)
        return True
    
    except False:
        print(f"File {name} not found.")
        return False


def rmdir(currentDirectory: Directory, name: str) -> bool:

    for file in currentDirectory.showDirectories():
        if file.name == name:
            currentDirectory.removeDirectory(name)
            return True
    
    print(f"Directory {name} not found.")
    return False

def ls(currentDirectory: Directory):
    '''
    Recieves a directory and prints the name and size of all files and directories in it.

    Parameters:
    currentDirectory: Directory
        The directory whose files and directories will be printed.

    Returns:
        None
    '''


    print("{:<30} {:<10}".format("Name", "Size"))
    print("-" * 40)


    for file in currentDirectory.showFiles():
        print(file.showInfo())

    for directory in currentDirectory.showDirectories():
        print(directory.showInfo())

def cd(user: User, targetDirectory: str):
    '''
    Recieves a user and a target directory name and changes the user's current directory to the target directory.

    Parameters:
    user: User
        The user whose current directory will be changed.
    targetDirectory: str
        The name of the target directory.
    
    Returns:
        bool
            True if the user's current directory was changed successfully, False if the target directory does not exist.

    '''

    for dir in user.currentPath.showDirectories():    
        if dir.name == targetDirectory:
            user.currentPath = dir
            return True
        
    raise IndexError
    return False

def whoami(user: User): 

    '''
    Recieves a user and prints the name of the user.

    Parameters:
    user: User
        The user whose name will be printed.

    Returns:
        None
    '''

    print(user.name)

def clear():
    '''
    Clears the terminal.
    '''

    print("\n" * 100)

def help():
    """
    Displays help information about available commands and their usage.
    """
    help_info = """
    Available commands:
    --------------------
    mkdir <directory_name>    : Create a new directory.
    touch <file_name>         : Create a new file.
    cd <directory_name>       : Change current directory.
    ls                        : List files and directories in the current directory.
    nano <file_name>          : Edit the content of a file.
    cat <file_name>           : Display the content of a file.
    whoami                    : Display the current user.
    clear                     : Clear the terminal screen.
    exit                      : Exit the terminal simulator.
    """
    print(help_info.strip())



def nano(user: User, filename: str):
    '''
    Recieves a user and a filename and changes the content of the file with the given name.
    
    Parameters:
    user: User
        The user who is changing the content of the file.
    filename: str
        The name of the file whose content will be changed.

    Returns:
        bool
            True if the content of the file was changed successfully, False if the file does not exist.
    '''


    for file in user.currentPath.showFiles():
        if file.name == filename:
            file = file
        else:
            print(f"File {filename} not found.")
            return False
    clear()
    user_input = input("Enter the content of the file; type 'exit()' to exit and save the file. \n\n")
    content = ""    
    while user_input != "exit()":
        content += user_input + "\n"
        user_input = input()

    file.changeContent(content)
    return True


def cat(user: User, filename: str):
    '''
    Recieves a user and a filename and prints the content of the file with the given name.

    Parameters:
    user: User
        The user who is printing the content of the file.
    filename: str
        The name of the file whose content will be printed.
    
    Returns:
        bool
            True if the content of the file was printed successfully, False if the file does not exist.
    '''
    for file in user.currentPath.showFiles():
            if file.name == filename:
                file = file
                print(file.showContent())
                return True 
            else:
                print(f"File {filename} not found.")
                return False




def switch(user_input: str, user: User):
    '''
    Recieves a user input, a directory and a user and executes the command given by the user.

    Parameters:
    user_input: str
        The command given by the user.
    user: User
        The user who is executing the command.
    
    Returns:
        User
    '''

    user_input = user_input.split(" ")

    if len(user_input) > 2:
        print("Invalid command. Please try again.\n")
        return user

    if "mkdir" in user_input:
        try:
            mkdir(user.currentPath, user_input[1])
        except FileExistsError:
            print(f"""Directory "{user_input[1]}"  already exists.""")

    elif "nano" in user_input:
        nano(user, user_input[1])

    elif "cat" in user_input:
        cat(user, user_input[1])

    elif "help" in user_input:
        help()

    elif "touch" in user_input:
        try:
            touch(user_input[1] , user.currentPath)
        except FileExistsError:
            print(f"""File "{user_input[1]}" already exists.""")

    elif "ls" in user_input:
        ls(user.currentPath)

    elif "rm" in user_input:
        rm(user.currentPath, user_input[1])

    elif "rmdir" in user_input:
        rmdir(user.currentPath, user_input[1])

    elif "cd" in user_input:
        if user_input[1] == "..":
            if user.currentPath.parent is None:
                print("You are in the root directory.")
                return user
            else:
                user.currentPath = user.currentPath.parent
                return user
        try:
            cd(user, user_input[1])

        except IndexError:
            print("Invalid command. Please try again.\n")
        
        return user

    elif "whoami" in user_input:
        whoami(user)

    elif "clear" in user_input:
        clear()

    elif "exit" in user_input:
        return

    else:
        print("Command not found. Please try again.\n")

    return user