
from pbf_python.Commands.insert_setup_package import InsertSetupPackage

from pbf.templates import template_manager
import os

class MakePyDir:
    """ Represents a command that makes a python directory """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('directory', action='store', help='Directory to create as a Python package')
        parser.add_argument('-i', '--install', action='store_true', help='Add the new package to the setup install file')
    
    def run(self, arguments):
        """ Run the command """
        dirname = arguments.directory
        install = arguments.install
        print "Creating Python Directory:", dirname
        self.makePyDir(dirname, install=install)
        
    def makePyDir(self, dirname, install=False):
        """ Create the Python directory """
        os.mkdir(dirname)
        template_manager.Save(os.path.join(dirname, "__init__.py"), [])
        
        if install:
            insertCommand = InsertSetupPackage()
            insertCommand.insertPackage(dirname)
