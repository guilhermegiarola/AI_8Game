import os

class eightGame:
    def __init__(self):
        self.table = []
        self.inserts = []
        
        while len(self.inserts) < 9:
            value = input()
            if value not in self.inserts and value == ' ':
                self.inserts.append(value)            
            elif value in self.inserts:
                print("Valor inválido!")
            elif int(value) < 0 or int(value) > 8:
                print("Valor inválido!")
            else:
                self.inserts.append(value)
                
        for i in range(0,3):
            self.table.append([])
        
        for i in range(0,3):
            for j in range(0,3):
                self.table[i].append(self.inserts.pop(0))
        
        os.system('clear')

        
    def amplitudeSearch(self):
        nodes = self.createQueue()
        while(len(nodes) > 0):
            table = nodes.pop(0)
            if(self.isFinal(table)):
                return table
            #nodes.append(expandSearch(table))
        return False
    
    def createQueue(self):
        nodes = []
        nodes.append(self.table)
        return nodes
    
    def printTable(self, table):
        for i in range(0,3):
            print(self.table[i][0] + " " + self.table[i][1] +
            " " + self.table[i][2])
        print()
    
    def isFinal(self, table):
        if(table[0][0] == '1' and
           table[0][1] == '2' and
           table[0][2] == '3' and
           table[1][0] == '8' and
           table[1][1] == ' ' and
           table[1][2] == '4' and
           table[2][0] == '7' and
           table[2][1] == '6' and
           table[2][2] == '5'):
            return True
        else:
            return False
    
if __name__ == '__main__':
    game = eightGame()
    game.amplitudeSearch()
    


                
                
