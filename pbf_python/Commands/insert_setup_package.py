from pbf.Commands import command_manager
from pbf.helpers.file_helper import GetLinesFromFile, Save
from pbf_python.helpers.python_helper import GetPythonPackageForFilename, GetPythonRootForFilename, FindSetupFilename

import os

class InsertSetupPackage:
    """ Represents a command to insert a Python package into the setup file """
    category = "insert"
    command = "setup-package"
    description = "Inserts a package into the setup package"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the command """
        dirname = args[0]
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
        packagePath = "'{0}'".format(GetPythonPackageForFilename(GetPythonRootForFilename(dirname), dirname))
        
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
        packagesString = lines[packagesLineNumber].split('[')[1]
        packagesEndLineNumber = packagesLineNumber
        
        if ']' in packagesString:
            packagesString = packagesString.split(']')[0]
        else:
            for i in range(packagesLineNumber, len(lines)):
                line = lines[i]
                if ']' in line:
                    packagesString += line.split(']')[0]
                    packagesEndLineNumber = i
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
        
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [package-directory]".format(category=self.category, command=self.command)
        print "Insert the package path to the given directory in the setup.py file"
    
command_manager.RegisterCommand(InsertSetupPackage)