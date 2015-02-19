from mk_pydir import MakePyDir
from new_setup import NewSetup

import os

class MkPyPackage:
    """ Command to create a Python Package """
                          
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Folder to create the package in')
        parser.add_argument('name', action='store', help='Name of the package to create')
    
    def run(self, arguments):
        """ Run the command """
        print "Creating package {0} at {1}".format(arguments.name, arguments.destination)
        self.makePackage(arguments.destination, arguments.name)
        
    def makePackage(self, destination, packageName):
        """ Make a Python package with the given name at the given destination """
        packageFolder = os.path.join(destination, packageName)
        MakePyDir().makePyDir(packageFolder)
        NewSetup().createSetup(destination, packageName)