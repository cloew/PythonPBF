from pbf.helpers.filename_helper import GetPythonClassnameFromFilename
from pbf.templates.template_loader import TemplateLoader
from pbf_python.templates import TemplatesRoot

class NewClass:
    """ Command to create a new Python class """
    TEMPLATE_LOADER = TemplateLoader("class.py", TemplatesRoot)
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the new Python class file')
    
    def run(self, arguments):
        """ Run the command """
        self.createClass(arguments.destination)
        
    def createClass(self, filepath):
        """ Create a Class """
        classname = GetPythonClassnameFromFilename(filename)
        self.TEMPLATE_LOADER.copy(filepath, keywords={"%ClassName%":classname})
