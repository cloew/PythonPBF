from pbf.Commands import command_manager

from pbf.Commands.Python.mk_pydir import MakePyDir as CoreMakePyDir

class MakePyDir:
    """ Represents a command that makes a python directory """
    category = "mk"
    command = "pydir"
    description = "Makes a Python Directory"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the command """
        dirname = args[0]
        print "Creating Python Directory:", dirname
        self.makePyDir(dirname)
        
    def makePyDir(self, dirname):
        """ Create the Python directory """
        CoreMakePyDir().makePyDir(dirname)
    
    def help(self):
        """ Print the usage of the Make Py Dir """
        print "Usage: pbf {category} {command} [path/to/dir]".format(category=self.category, command=self.command)
        print "\tWill create a Python Directory called [name] at the path given"
    
command_manager.RegisterCommand(MakePyDir)