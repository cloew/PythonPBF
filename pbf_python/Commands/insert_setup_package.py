from pbf_python.helpers.python_helper import GetPythonPackageForFilename, FindSetupFilename
from .add_value_to_py_list import AddValueToPyList

import os

class InsertSetupPackage:
    """ Represents a command to insert a Python package into the setup file """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('directory', action='store', help='Package Directory to add to setup.py file')
    
    def run(self, arguments):
        """ Run the command """
        dirname = arguments.directory
        self.insertPackage(dirname)
        
    def insertPackage(self, dirname):
        """ Insert the package for the given directory into setup.py """
        setupFilename = FindSetupFilename(dirname)
        if os.path.exists(setupFilename):
            self.updateSetupFile(dirname, setupFilename)
        else:
            print "No setup file found"
        
    def updateSetupFile(self, dirname, setupFilename):
        """ Update the setup file """
        packagePath = "'{0}'".format(GetPythonPackageForFilename(dirname))
        AddValueToPyList().addValue('packages', packagePath, setupFilename)