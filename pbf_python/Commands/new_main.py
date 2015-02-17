from pbf.templates.template_loader import TemplateLoader
from pbf_python.templates import TemplatesRoot

class NewMain:
    """ Creates a new Python Main file """
    TEMPLATE_LOADER = TemplateLoader("main.py", TemplatesRoot, defaultFilename="main.py")
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the main file')
    
    def run(self, arguments):
        """ Run the Command """
        destination = arguments.destination
        print "Creating Python main at:", destination
        self.makeMain(destination)
        
    def makeMain(self, filepath):
        """ Makes the main file at the given location """
        self.TEMPLATE_LOADER.copy(filepath)
