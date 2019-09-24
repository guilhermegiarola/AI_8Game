from node import Node
from copy import deepcopy
import time
import queue
import os

class eightGame:
    def __init__(self):
        self.rootNode = Node()
        
        while len(self.rootNode.getTable()) < 9:
            value = input()
            if value not in self.rootNode.getTable() and value == ' ':
                self.rootNode.getTable().append(value)            
            elif value in self.rootNode.getTable():
                print("Valor inválido!")
            elif int(value) < 0 or int(value) >= 9:
                print("Valor inválido!")
            else:
                self.rootNode.getTable().append(value)
        os.system('clear')

    def printTable(self, node):
        table = node.getTable()
        for i in range(0,3):
            print(table[i*3] + " " + table[i*3+1] + " "
                  + table[i*3+2])
        print()
    
    #Debug this:
    def breadthFirstSearch(self, node):
        nodes = []
        nodes.append(node)
        
        while len(nodes) > 0:
            aux = nodes.pop(0)
            if self.isFinal(aux):
                print("Encontrado!")
                self.printTable(aux)
                return aux
            for i in self.expandTree(aux):
                nodes.append(i)


    #Debug this:
    def expandTree(self, node):
        emptyPosition = 0
        
        auxNode1 = Node()
        auxNode2 = Node()
        auxNode3 = Node()
        auxNode4 = Node()
        auxTable = deepcopy(node.getTable())
        
        expandedList = []
        firstGroup = [0,1,3,4,6,7]
        secondGroup = [0,1,2,3,4,5]
        thirdGroup = [1,2,4,5,7,8]
        forthGroup = [3,4,5,6,7,8]

        # range(a, b) retorna [a, a+1, a+2...a+n, b]
        for i in range(0,len(node.getTable())):
            if auxTable[i] == '0':
                emptyPosition = i

        for i in firstGroup:
            if emptyPosition == i:
                auxTable = deepcopy(node.getTable())
                auxTable[i], auxTable[i+1] = auxTable[i+1], auxTable[i]
                auxNode1.setTable(auxTable)
                self.printTable(auxNode1)
                expandedList.append(auxNode1)
        auxTable = deepcopy([])

        for i in secondGroup:
            if emptyPosition == i:
                auxTable = deepcopy(node.getTable())
                auxTable[i], auxTable[i+3] = auxTable[i+3], auxTable[i]
                auxNode2.setTable(auxTable)
                self.printTable(auxNode2)
                expandedList.append(auxNode2)
        auxTable = deepcopy([])

        for i in thirdGroup:
            if emptyPosition == i:
                auxTable = deepcopy(node.getTable())
                auxTable[i], auxTable[i-1] = auxTable[i-1], auxTable[i]
                auxNode3.setTable(auxTable)
                self.printTable(auxNode3)
                expandedList.append(auxNode3)
        
        auxTable = deepcopy([])
        for i in forthGroup:
            if emptyPosition == i:
                auxTable = deepcopy(node.getTable())
                auxTable[i], auxTable[i-3] = auxTable[i-3], auxTable[i]
                auxNode4.setTable(auxTable)
                self.printTable(auxNode4)
                expandedList.append(auxNode4)

        return expandedList
            

    def swap(num1, num2):
        aux = num1
        num1 = num2
        num2 = aux

    def isFinal(self, node):
        table = node.getTable()
        if(table[0] is '1' and
           table[1] is '2' and
           table[2] is '3' and
           table[3] is '8' and
           table[4] is '0' and
           table[5] is '4' and
           table[6] is '7' and
           table[7] is '6' and
           table[8] is '5'):
            return True
        else:
            return False
        
def main():
    game = eightGame()
    game.breadthFirstSearch(game.rootNode)

if __name__ == "__main__":
    main()