from pbf.Commands import command_manager
from pbf.helpers.filename_helper import GetPythonClassnameFromFilename
from pbf_python.templates import TemplatesRoot
from pbf.templates import template_manager

class NewClass:
    """ Command to create a new Python class """
    category = "new"
    command = "class"
    description = "Create a new Python Class"
    
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
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path/to/class]".format(category=self.category, command=self.command)
        print "Create a Python class at the path specified"
    
command_manager.RegisterCommand(NewClass)