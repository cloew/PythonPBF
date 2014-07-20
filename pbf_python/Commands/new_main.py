from pbf.Commands import command_manager
from pbf.helpers.file_helper import IsDirectory
from pbf_python.templates import TemplatesRoot
from pbf.templates import template_manager

import os

class NewMain:
    """ Creates a new Python Main file """
    category = "new"
    command = "main"
    description = "Create a new Python main file"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the main file')
    
    def run(self, arguments):
        """ Run the Command """
        destination = arguments.destination
        print "Creating Python main at:", destination
        self.makeMain(destination)
        
    def makeMain(self, file):
        """ Makes the main file at the given location """
        if IsDirectory(file):
            file = os.path.join(file, "main.py")
        template_manager.CopyTemplate(file, "main.py", templates_directory=TemplatesRoot)
    
    def help(self):
        """ Print the Usage of the New Main Command """
        print "Usage: pbf {category} {command} [path/to/main.py]".format(category=self.category, command=self.command)
        print "\tWill create a main.py file at the location given"
    
command_manager.RegisterCommand(NewMain)