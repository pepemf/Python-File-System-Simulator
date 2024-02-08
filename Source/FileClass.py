class File:
    def __init__(self, name: str):
            """
            Initializes a new instance of the FileClass.

            Args:
                name (str): The name of the file.

            """
            self.name = name
            self.content = ""
            self.size = self.__calculateSize(self.content)


    def __calculateSize(self, content):
        self.size = len(content)
        return self.size

    def changeContent(self, content: str):
        self.content = content

        self.size = self.__calculateSize(self.content)

    def showContent(self):
        return self.content
    
    def showInfo(self):
        return "{:<30} {:<10}".format(self.name, f"{self.size} bytes")
    

    

    