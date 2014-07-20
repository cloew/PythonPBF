from pbf.Commands import command_manager

from pbf_python.Commands.insert_setup_package import InsertSetupPackage

from pbf.templates import template_manager
import os

class MakePyDir:
    """ Represents a command that makes a python directory """
    category = "mk"
    command = "pydir"
    description = "Makes a Python Directory"
    
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
    
    def help(self):
        """ Print the usage of the Make Py Dir """
        print "Usage: pbf {category} {command} [path/to/dir]".format(category=self.category, command=self.command)
        print "\tWill create a Python Directory called [name] at the path given"
    
command_manager.RegisterCommand(MakePyDir)