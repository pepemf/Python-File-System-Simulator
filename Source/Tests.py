import unittest
from Source.DirectoryClass import Directory
from Source.User import User
from Source.Binaries import mkdir, touch, cd

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.user = User("test_user", Directory("/"))
        self.root_directory = Directory("/")

    def test_mkdir(self):
        mkdir(self.root_directory, "test_dir")
        self.assertTrue(any(d.name == "test_dir" for d in self.root_directory.subdirectories))

    def test_touch(self):
        touch("test_file.txt", self.root_directory)
        self.assertTrue(any(f.name == "test_file.txt" for f in self.root_directory.files))

    def test_cd(self):
        mkdir(self.root_directory, "test_dir")
        test_user = User("test_user", self.root_directory)
        direct = self.root_directory.subdirectories[0]
        cd(test_user, test_user.currentPath.subdirectories[0].name)
        self.assertEqual(direct.name, test_user.currentPath.name)

    def test_whoami(self):
        test_user = User("test_user", self.root_directory)
        self.assertEqual(test_user.name, "test_user")
            
    

if __name__ == '__main__':
    unittest.main(verbosity=2)
