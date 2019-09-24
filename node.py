class Node:
    def __init__(self):
        self.nodeSons = []
        self.nodeTable = []
    
    def getTable(self):
        copiedTable = self.nodeTable
        return copiedTable
    
    def getTableItem(self, position):
        return self.nodeTable[position]
    
    def setTable(self, table):
        del(self.nodeTable)
        self.nodeTable = table
    
    def setTableItem(self,position, value):
        self.nodeTable[position] = value
    
    def setSon(self, node):
        self.nodeSons.append(node)