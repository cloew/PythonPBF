
class PythonListDetector:
    """ Represents a method of detecting for a specifically named Python List in a Python file """
    
    def __init__(self, varName):
        """ Initialize the Detector with the variable it should detect """
        self.varName = varName
    
    def isStart(self, line):
        """ Return if this line is the start of the requested list """
        return self.varName in line
        
    def isEnd(self, line):
        """ Return if this is the the end of the requested list """
        return ']' in line