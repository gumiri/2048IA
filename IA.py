import math
import random
from game_2048 import Game 

class GameBackground:
    def __init__(self):
        self.cells = []
        self.start_game()
        

    def start_game(self):
        #create matrix of zeros
        self.matrix = [[0] *4 for _ in range (4)]

        #fill 2 random cells with 2s
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        self.matrix[row][col] = 2

        while (self.matrix[row][col] != 0):
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        self.matrix[row][col] = 2

        self.score = 0
        self.simulatedScore = 0
        self.simulatedMatrix = self.matrix

    def restartSimulation(self):
        self.simulatedMatrix = self.matrix

    def stack(self, simulation):
        new_matrix = [[0] *4 for _ in range(4)]
        if (simulation):
            for i in range(4):
                fill_position = 0
                for j in range(4):
                    if self.simulatedMatrix[i][j] != 0:
                        new_matrix[i][fill_position] = self.simulatedMatrix[i][j]
                        fill_position += 1

            self.simulatedMatrix = new_matrix
        else:
            for i in range(4):
                fill_position = 0
                for j in range(4):
                    if self.matrix[i][j] != 0:
                        new_matrix[i][fill_position] = self.matrix[i][j]
                        fill_position += 1

            self.matrix = new_matrix
            self.simulatedMatrix = self.matrix

    def combine(self, simulation):
        if (simulation):
            for i in range(4):
                for j in range(3):
                    if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                        self.simulatedMatrix[i][j] *= 2
                        self.simulatedMatrix[i][j + 1] = 0
                        self.simulatedScore += self.simulatedMatrix[i][j]

        else:
            for i in range(4):
                for j in range(3):
                    if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                        self.matrix[i][j] *= 2
                        self.matrix[i][j + 1] = 0
                        self.score += self.matrix[i][j]
                        self.simulatedMatrix = self.matrix


    def reverse(self, simulation):
        new_matrix = []
        if (simulation):
            for i in range(4):
                new_matrix.append([])
                for j in range(4):
                    new_matrix[i].append(self.simulatedMatrix[i][3 - j])

            self.simulatedMatrix = new_matrix
 
        else:
            for i in range(4):
                new_matrix.append([])
                for j in range(4):
                    new_matrix[i].append(self.matrix[i][3 - j])

            self.matrix = new_matrix
            self.simulatedMatrix = self.matrix

    def transpose(self, simulation):
        new_matrix = [[0] *4 for _ in range(4)]
        if (simulation):
            for i in range(4):
                for j in range(4):
                    new_matrix[i][j] = self.simulatedMatrix[j][i]

            self.simulatedMatrix = new_matrix
        else:
            for i in range(4):
                for j in range(4):
                    new_matrix[i][j] = self.matrix[j][i]

            self.matrix = new_matrix
            self.simulatedMatrix = self.matrix


    def matrix_full(self, simulation):
        full = 0
        if (simulation):
            for i in range(4):
                for j in range(4):
                    if self.simulatedMatrix[i][j] == 0:
                        return False
            return True
        else:
            for i in range(4):
                for j in range(4):
                    if self.matrix[i][j] == 0:
                        return False
            return True

    def add_new_tile(self, simulation):
        if (simulation):
            if not self.matrix_full(simulation):
                row = random.randint(0, 3)
                col = random.randint(0, 3)
                while (self.simulatedMatrix[row][col] != 0):
                    row = random.randint(0, 3)
                    col = random.randint(0, 3)
                self.simulatedMatrix[row][col] = random.choice([2, 4])
        else:
            if not self.matrix_full(simulation):
                row = random.randint(0, 3)
                col = random.randint(0, 3)
                while (self.matrix[row][col] != 0):
                    row = random.randint(0, 3)
                    col = random.randint(0, 3)
                self.matrix[row][col] = random.choice([2, 4])

    def left(self, simulation):
        self.stack(simulation)
        self.combine(simulation)
        self.stack(simulation)
        self.add_new_tile(simulation)
        self.gameOverWin(simulation)
        self.gameOverLose(simulation)

    def right(self, simulation):
        self.reverse(simulation)
        self.stack(simulation)
        self.combine(simulation)
        self.stack(simulation)
        self.reverse(simulation)
        self.add_new_tile(simulation)
        self.gameOverWin(simulation)
        self.gameOverLose(simulation)

    def up(self, simulation):
        self.transpose(simulation)
        self.stack(simulation)
        self.combine(simulation)
        self.stack(simulation)
        self.transpose(simulation)
        self.add_new_tile(simulation)
        self.gameOverWin(simulation)
        self.gameOverLose(simulation)

    def down(self, simulation):
        self.transpose(simulation)
        self.reverse(simulation)
        self.stack(simulation)
        self.combine(simulation)
        self.stack(simulation)
        self.reverse(simulation)
        self.transpose(simulation)
        self.add_new_tile(simulation)
        self.gameOverWin(simulation)
        self.gameOverLose(simulation)

    def horizontal_move_exists(self, simulation):
        if (simulation):
            for i in range(4):
                for j in range(3):
                    if self.simulatedMatrix[i][j] == self.simulatedMatrix[i][j + 1]:
                        return True
            return False
        else:
            for i in range(4):
                for j in range(3):
                    if self.matrix[i][j] == self.matrix[i][j + 1]:
                        return True

            return False

    def vertical_move_exists(self, simulation):
        if (simulation):
            for i in range(3):
                for j in range(4):
                    if self.simulatedMatrix[i][j] == self.simulatedMatrix[i + 1][j]:
                        return True
            return False
        else:
            for i in range(3):
                for j in range(4):
                    if self.matrix[i][j] == self.matrix[i + 1][j]:
                        return True

            return False

    def gameOverWin(self, simulation):
        if (simulation):
            if any(2048 in row for row in self.simulatedMatrix):
                print("Winnerrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
                return True
            return False
        else:
            if any(2048 in row for row in self.matrix):
                print("Winnerrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
                return True
            return False

    def gameOverLose(self, simulation):
        if (simulation):
            if not any(0 in row for row in self.simulatedMatrix) and not self.horizontal_move_exists(simulation) and not self.vertical_move_exists(simulation):
                return True
            return False
        else:
            if not any(0 in row for row in self.matrix) and not self.horizontal_move_exists(simulation) and not self.vertical_move_exists(simulation):
                return True
            return False


class Node:
    def __init__(self, state):
        self.state = state
        #t = score
        self.w = 1
        self.g = 1
        self.t = 0
        #n = número de vezes visitadas
        self.n = 0
        self.pev = None
        self.right = None
        self.left = None
        self.up = None
        self.down = None

class Tree:
    def __init__(self, node):
        self.root = node
        self.game = GameBackground()

    def addNodes(self, root):
        leftNode = Node("left")
        leftNode.prev = root
        root.left = leftNode
        rightNode = Node("right")
        rightNode.prev = root
        root.right = rightNode
        downNode = Node("down")
        downNode.prev = root
        root.down = downNode
        upNode = Node("up")
        upNode.prev = root
        root.up = upNode

    def makeMoves(self):
        while (self.root != None):
            if (self.root.left.t > self.root.right.t and self.root.left.t > self.root.up.t and self.root.left.t > self.root.down.t):
                game.left()
                self.root = self.root.left
            elif (self.root.right.t > self.root.left.t and self.root.right.t > self.root.up.t and self.root.right.t > self.root.down.t):
                game.right()
                self.root = self.root.right
            elif (self.root.up.t > self.root.right.t and self.root.up.t > self.root.left.t and self.root.up.t > self.root.down.t):
                game.up()
                self.root = self.root.up
            elif (self.root.down.t > self.root.right.t and self.root.down.t > self.root.up.t and self.root.down.t > self.root.left.t):
                game.down()
                self.root = self.root.down





    def toString(self):
        aux = self.root
        r = ""
        while (aux != None):
            r += aux.move + ", "
            aux = aux.prev

        return r




class IA:
    def __init__(self):
        self.possibleStates = ["left", "right", "up", "down"]
        self.tree = Tree(Node(self.possibleStates[random.randint(0,3)]))
        self.expand(self.tree.root)
        self.avg = 0
        self.soma = 0

    def simulation(self, state):
        if (state == "left"):
            self.tree.game.left(True)
        elif (state == "right"):
            self.tree.game.right(True)
        elif (state == "up"):
            self.tree.game.up(True)
        elif (state == "down"):
            self.tree.game.down(True)

        print("Até aqui tbm")
        while True:
            if (self.tree.game.gameOverWin(False) == False and self.tree.game.gameOverLose(False) == False):
                nextMove = self.possibleStates[random.randint(0,3)]
                if (nextMove == "left"):
                    self.tree.game.left(False)
                elif (nextMove == "right"):
                    self.tree.game.right(False)
                elif (nextMove == "up"):
                    self.tree.game.up(False)
                elif (nextMove == "down"):
                    self.tree.game.down(False)

                print(nextMove)

            else:
                break

        return self.tree.game.simulatedScore


    def bestChoice(self, moved):
       pass 



    def select(self):
        node = self.tree.root
        while (self.isLeafNode(node) == False):
            if (node.left.n < 1):
                node = node.left
            elif (node.right.n < 1):
                node = node.right
            elif (node.up.n < 1):
                node = node.up
            elif (node.down.n < 1):
                node = node.down
            else:
                calc1 = (node.left.t / node.left.n) + 2*(math.sqrt(math.log(node.left.prev.n)/node.left.n))
                calc2 = (node.right.t/ node.right.n) + 2*(math.sqrt(math.log(node.right.prev.n)/node.right.n))
                calc3 = (node.up.t / node.up.n) + 2*(math.sqrt(math.log(node.up.prev.n)/node.up.n))
                calc4 = (node.down.t / node.down.n) + 2*(math.sqrt(math.log(node.down.prev.n)/node.down.n))

                
                #print(calc1)
                #print(calc2)
                #print(calc3)
                #print(calc4)
                if (calc1 > calc2 and calc1 > calc3 and calc1 > calc4):
                    node = node.left
                    #print("calc1")
                    #print(node.prev.n)
                    #print(node.n)
                elif (calc2 > calc1 and calc2 > calc3 and calc2 > calc4):
                    node = node.right
                    #print("calc2")
                    #print(node.prev.n)
                    #print(node.n)
                elif (calc3 > calc1 and calc3 > calc2 and calc3 > calc4):
                    node = node.up
                    #print("calc3")
                    #print(node.prev.n)
                    #print(node.n)
                elif (calc4 > calc1 and calc4 > calc2 and calc4 > calc3):
                    node = node.down
                    #print("calc4")
                    #print(node.prev.n)
                    #print(node.n)
                else:
                    if (node.left.n > node.right.n):
                        node = node.right
                    elif (node.right.n > node.up.n):
                        node = node.up
                    elif (node.up.n > node.down.n):
                        node = node.down
                    else:
                        node = node.left

        
        if (node.n < 1):
            self.avg += 1
            self.soma += self.simulation(node.state) /2
            print(self.average(self.soma, self.avg) *2)

        else:
            self.expand(node)
            self.tree.makeMoves()

            
    
    def average(self, soma, avg):
        return soma / avg
            


    def expand(self, root):
        self.tree.addNodes(root)

    def move(self, nome):
        if (nome == "left"):
            self.gamebg.left()
        elif (nome == "right"):
            self.gamebg.right()
        elif (nome == "up"):
            self.gamebg.up()
        elif (nome == "down"):
            self.gamebg.down()

    def isLeafNode(self, node):
        if(node.right == None or node.left == None or node.up == None or node.down == None):
            return True
        return False



def main():
    ia = IA()
    times = 1
    count = 0
    while(True):
        ia.select()
        count += 1
    

main()
