from DirectoryClass import Directory


class User:
    def __init__(self, name, currentPath: Directory) -> None:

        self.name = name
        self.currentPath = currentPath
        pass
