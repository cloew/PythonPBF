from kao_decorators import proxy_for

@proxy_for('values', ['append'])
class PythonList:
    """ Represents a Python list in a file """
    
    def __init__(self, listSection):
        """ Initialize the Python List with the list section it should read values from """
        self.listHeader = listSection[0].split('[')[0]
        self.afterList = listSection[-1].split(']')[1]
        listString = self.buildListString(listSection)
        self.values = [value.strip() for value in listString.split(',')]
        
    def buildListString(self, section):
        """ Consolidate lines to just be the text within the list start and stop """
        if len(section) == 1:
            return section[0].split('[')[1].split(']')[0]
        else:
            return "{0}{1}{2}".format(section[0].split('[')[1], ''.join(section[1:-1]), section[-1].split(']')[0])
            
    def toLines(self):
        """ Convert this list to lines """
        indentLength = len(self.listHeader) + 1
        leadingWhitespace = ' '*indentLength
        valuesText = ",\n{0}".format(leadingWhitespace).join(self.values)
        fullListString = "{0}[{1}]{2}".format(self.listHeader, valuesText, self.afterList)
        return fullListString.split('\n')