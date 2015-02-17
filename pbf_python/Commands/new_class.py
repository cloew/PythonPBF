from pbf.helpers.filename_helper import GetPythonClassnameFromFilename
from pbf_python.templates import TemplatesRoot
from pbf.templates import template_manager

class NewClass:
    """ Command to create a new Python class """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the new Python class file')
    
    def run(self, arguments):
        """ Run the command """
        self.createClass(arguments.destination)
        
    def createClass(self, filename):
        """ Create a Class """
        classname = GetPythonClassnameFromFilename(filename)
        template_manager.CopyTemplate(filename, "class.py", {"%ClassName%":classname}, TemplatesRoot)
