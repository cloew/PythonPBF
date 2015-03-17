from pbf.helpers.file_helper import GetLinesFromFile, Save
from pbf_python.helpers.python_helper import GetPythonPackageForFilename, GetPythonRootForFilename, FindSetupFilename

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
        originalLines = GetLinesFromFile(setupFilename)
        packagePath = "'{0}'".format(GetPythonPackageForFilename(dirname))
        
        packagesLineNumber = self.findPackagesLineNumber(originalLines)
        packagesEndLineNumber = None
        
        originalPackageStringHeader = originalLines[packagesLineNumber].split('[')[0]
        whitespaceLength = len(originalPackageStringHeader) + 1
        packagesString, packagesEndLineNumber = self.buildPackagesString(originalLines, packagesLineNumber)
        
        packages = self.getPackages(packagesString)
        packages.append(packagePath)
        
        newLines = list(originalLines)
        newLines[packagesLineNumber:packagesEndLineNumber+1] = self.buildPackagesStringList(originalPackageStringHeader, packages, whitespaceLength)
        
        Save(setupFilename, newLines)
        
    def getPackages(self, packagesString):
        """ Return the packages """
        return [package.strip() for package in packagesString.split(',')]
        
    def buildPackagesString(self, lines, packagesLineNumber):
        """ Build Packages String """
        firstLine = lines[packagesLineNumber].split('[')[1]
        lines = [firstLine] + lines[packagesLineNumber+1:]
        
        packagesString = ''
        packagesEndLineNumber = packagesLineNumber
        
        for i, line in enumerate(lines):
            if ']' in line:
                packagesString += line.split(']')[0]
                packagesEndLineNumber = i + packagesLineNumber
                break
            else:
                packagesString += line
                
        return packagesString, packagesEndLineNumber
        
    def buildPackagesStringList(self, originalPackageStringHeader, packages, whitespaceLength):
        """ Return the strings for the Packages """
        firstPackage = "{0}[{1},\n".format(originalPackageStringHeader, packages[0])
        middlePacakges = ["{0}{1},\n".format(' '*whitespaceLength, packageString.strip()) for packageString in packages[1:-1]]
        lastPackage = "{0}{1}],\n".format(' '*whitespaceLength, packages[-1].strip())
        return [firstPackage] + middlePacakges + [lastPackage]
        
    def findPackagesLineNumber(self, lines):
        """ Return the line the packages are generated on """
        for i in range(len(lines)):
            if "packages" in lines[i]:
                return i
        return None
        
