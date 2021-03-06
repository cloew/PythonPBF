from pbf.helpers.file_helper import IsDirectory
from pbf.helpers.filename_helper import GetBaseFilenameWithoutExtension, RemoveFileExtension

import os

def GetPythonPackageForFilename(filename, rootDirectory=None):
    """ Return the Python Package Path for the given filename from the given Python root """
    if rootDirectory is None:
        rootDirectory = GetPythonRootForFilename(filename)
        
    if rootDirectory is not None:
        path = os.path.relpath(filename, rootDirectory)
        path = RemoveFileExtension(path)
        path = path.replace("/", ".")
        return path.replace("\\", ".")
    else:
        return GetBaseFilenameWithoutExtension(filename)
    
def GetPythonImportString(filenameToImportFrom, imports, asName=None):
    """ Constructs and returns a Python Import Line """
    package = GetPythonPackageForFilename(filenameToImportFrom)
    asString = ""
    
    if asName is not None and len(imports) == 1:
        asString = " as {0}".format(asName)
    
    importString = "from {0} import {1}{2}\n".format(package, ", ".join(imports), asString)
    return importString
    
def GetPythonPackageRootForFilename(filename):
    """ Returns the Python Package Root that the filename is in or None """
    absolutePathToFilename = os.path.abspath(filename)
    
    currentPath = absolutePathToFilename
    lastDirectory = None
    while True:
        directory = os.path.dirname(currentPath)
        if not IsPythonDirectory(directory):
            return lastDirectory
        lastDirectory = directory
        currentPath = directory
    
def GetPythonRootForFilename(filename):
    """ Returns the Python Project Root that the filename is in or None """
    absolutePathToFilename = os.path.abspath(filename)
    
    currentPath = absolutePathToFilename
    while True:
        directory = os.path.dirname(currentPath)
        if not IsPythonDirectory(directory):
            return directory
        currentPath = directory
        
def FindSetupFilename(dirname):
    """ Return the Setup Filename """
    root = GetPythonRootForFilename(dirname)
    return os.path.join(root, 'setup.py')
        
def IsPythonDirectory(directory):
    """ Return if the directory is a Python directory """
    initFilePath = os.path.join(directory, "__init__.py")
    return IsDirectory(directory) and os.path.exists(initFilePath)