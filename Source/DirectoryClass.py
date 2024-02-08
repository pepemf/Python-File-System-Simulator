from FileClass import File


class Directory:
    def __init__(self, name):
        """
        Initialize a Directory object.

        Args:
            name (str): The name of the directory.

        Attributes:
            name (str): The name of the directory.
            parent (Directory): The parent directory.
            files (list): List of files in the directory.
            subdirectories (list): List of subdirectories in the directory.
        """
        self.name = name
        self.parent = None
        self.files = []
        self.subdirectories = []

    def addFile(self, fileName: str):

        if fileName in [file.name for file in self.files]:
            raise FileExistsError
            return False

        file = File(fileName)
        self.files.append(file)
    
    def addDirectory(self, dirName: str):

        if dirName in [dir.name for dir in self.subdirectories]:
            raise FileExistsError
            return False

        directory = Directory(dirName)
        directory.parent = self

        self.subdirectories.append(directory)
        return True

    def removeFile(self, fileName: str) -> bool:

        file = self.findFile(fileName)

        if file is not None:
            self.files.remove(file)
            return True

        return False
    
    def removeDirectory(self, dirName: str) -> bool:
        
        for dir in self.subdirectories:
            if dir.name == dirName:
                self.subdirectories.remove(dir)
                return True
        return False
    
    def showFiles(self) -> list:

        return self.files
    
    def showDirectories(self) -> list:

        return self.subdirectories
    
    def findFile(self, fileName: str):
        for file in self.files:
            if file.name == fileName:
                return file
        return None
    
    def findDirectory(self, dirName: str):
        for dir in self.subdirectories:
            if dir.name == dirName:
                return dir
        return None

    def showInfo(self) -> str:
        return "{:<30} {:<10}".format(self.name + "/", "-")


    
            