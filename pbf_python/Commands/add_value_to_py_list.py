from pbf_python.helpers.python_list import PythonList
from pbf_python.helpers.python_list_detector import PythonListDetector

from kao_file import KaoFile, SectionFinder

class AddValueToPyList:
    """ Command to add a value to a python list in a file """
                          
    def addArguments(self, parser):
        """ Add arguments to the parser """
        pass # No Arguments
    
    def run(self, arguments):
        """ Run the command """
        
    def addValue(self, listName, value, filename, destination=None):
        """ Adds the value to the given list """
        if destination is None:
            destination = filename
        
        file = KaoFile.open(filename)
        listSection = SectionFinder(PythonListDetector(listName)).find(file, direction=SectionFinder.UP)
        
        if listSection is None:
            print("Unable to find List: {0}".format(listName))
        else:
            pythonList = PythonList(listSection)
            pythonList.append(value)
            
            file.replaceSection(listSection, pythonList.toLines())
            file.save(destination)