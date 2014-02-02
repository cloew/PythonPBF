from pbf.Commands import command_manager
from pbf.helpers.file_helper import IsDirectory
from pbf.python.templates import TemplatesRoot
from pbf.templates import template_manager

import os

class NewMain:
    """ Creates a new Python Main file """
    category = "new"
    command = "main"
    description = "Create a new Python main file"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the Command """
        print "Creating Python main at:", args[0]
        self.makeMain(args[0])
        
    def makeMain(self, file):
        """ Makes the main file at the given location """
        if IsDirectory(file):
            file = os.path.join(file, "main.py")
        template_manager.CopyTemplate(file, "Python/main.py", templates_directory=TemplatesRoot)
    
    def help(self):
        """ Print the Usage of the New Main Command """
        print "Usage: pbf {category} {command} [path/to/main.py]".format(category=self.category, command=self.command)
        print "\tWill create a main.py file at the location given"
    
command_manager.RegisterCommand(NewMain)