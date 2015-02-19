from pbf.templates.template_loader import TemplateLoader
from pbf_python.templates import TemplatesRoot

class NewSetup:
    """ Command to create a new Python Setup script """
    TEMPLATE_LOADER = TemplateLoader("setup.py", TemplatesRoot, defaultFilename="setup.py")
        
    def createSetup(self, filepath, packageName):
        """ Create a Setup """
        keywords = {"%PackagePath%":packageName}
        self.TEMPLATE_LOADER.copy(filepath, keywords=keywords)