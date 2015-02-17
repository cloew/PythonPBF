from pbf.helpers.file_helper import IsDirectory
from pbf_python.templates import TemplatesRoot
from pbf.templates import template_manager

import os

class NewMain:
    """ Creates a new Python Main file """
    
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
