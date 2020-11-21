import math
import random

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
        self.simulatedScore = self.score

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
                    if self.simulatedMatrix[i][j] != 0 and self.simulatedMatrix[i][j] == self.simulatedMatrix[i][j + 1]:
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
                print("Loser")
                return True
            return False
        else:
            if not any(0 in row for row in self.matrix) and not self.horizontal_move_exists(simulation) and not self.vertical_move_exists(simulation):
                print("Loser")
                return True
            return False


class Node:
    def __init__(self, state):
        self.state = state
        #t = score
        self.t = 0
        #n = número de vezes visitadas
        self.n = 0
        self.prev = None
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
        while (self.root.left != None and self.root.right != None and self.root.up != None and self.root.down != None):
            #print("left: {}".format(self.root.left.t))
            #print("right: {}".format(self.root.right.t))
            #print("up: {}".format(self.root.up.t))
            #print("down: {}".format(self.root.down.t))
            if (self.root.left.t > self.root.right.t and self.root.left.t > self.root.up.t and self.root.left.t > self.root.down.t):
                self.game.left(False)
                self.root = self.root.left
            elif (self.root.right.t > self.root.left.t and self.root.right.t > self.root.up.t and self.root.right.t > self.root.down.t):
                self.game.right(False)
                self.root = self.root.right
            elif (self.root.up.t > self.root.right.t and self.root.up.t > self.root.left.t and self.root.up.t > self.root.down.t):
                self.game.up(False)
                self.root = self.root.up
            elif (self.root.down.t > self.root.right.t and self.root.down.t > self.root.up.t and self.root.down.t > self.root.left.t):
                self.game.down(False)
                self.root = self.root.down
            else:
                break


        self.game.restartSimulation()





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
        node = Node(self.possibleStates[random.randint(0,3)])
        self.tree = Tree(node)
        self.expand(self.tree.root)
        self.avg = 0
        self.soma = 0

    def simulation(self):
        #if (state == "left"):
        #    self.tree.game.left(True)
        #elif (state == "right"):
        #    self.tree.game.right(True)
        #elif (state == "up"):
        #    self.tree.game.up(True)
        #elif (state == "down"):
        #    self.tree.game.down(True)

        while True:
            if (self.tree.game.gameOverWin(True) == False and self.tree.game.gameOverLose(True) == False):
               self.bestChoice()
                #nextMove = self.possibleStates[random.randint(0,3)]
                #if (nextMove == "left"):
                #    self.tree.game.left(True)
                #elif (nextMove == "right"):
                #    self.tree.game.right(True)
                #elif (nextMove == "up"):
                #    self.tree.game.up(True)
                #elif (nextMove == "down"):
                #    self.tree.game.down(True)
            else:
                break
        self.tree.game.restartSimulation()
        


        return self.tree.game.simulatedScore


    def bestChoice(self):
        maiorScore = 0
        bestMove = "left"
        self.tree.game.left(True)
        if (self.tree.game.simulatedScore > maiorScore):
            maiorScore = self.tree.game.simulatedScore
            bestMove = "left"
        self.tree.game.restartSimulation()
        self.tree.game.right(True)
        if (self.tree.game.simulatedScore > maiorScore):
            maiorScore = self.tree.game.simulatedScore
            bestMove = "right"
        self.tree.game.restartSimulation()
        self.tree.game.up(True)
        if (self.tree.game.simulatedScore > maiorScore):
            maiorScore = self.tree.game.simulatedScore
            bestMove = "up"
        self.tree.game.restartSimulation()
        self.tree.game.down(True)
        if (self.tree.game.simulatedScore > maiorScore):
            maiorScore = self.tree.game.simulatedScore
            bestMove = "down"
        self.tree.game.restartSimulation()
        
        if (bestMove == "left"):
            self.tree.game.left(True)
        elif (bestMove == "right"):
            self.tree.game.right(True)
        elif (bestMove == "up"):
            self.tree.game.up(True)
        elif (bestMove == "down"):
            self.tree.game.right(True)



        
        return bestMove




    def select(self):
        node = self.tree.root
        while (self.isLeafNode(node) == False):
            if (node.left.n < 1):
                node = node.left
            elif (node.down.n < 1):
                node = node.down
            elif (node.right.n < 1):
                node = node.right
            elif (node.up.n < 1):
                node = node.up
            else:
                calc1 = (node.left.t / node.left.n) + 2*(math.sqrt(math.log(node.left.prev.n)/node.left.n))
                calc2 = (node.right.t/ node.right.n) + 2*(math.sqrt(math.log(node.right.prev.n)/node.right.n))
                calc3 = (node.up.t / node.up.n) + 2*(math.sqrt(math.log(node.up.prev.n)/node.up.n))
                calc4 = (node.down.t / node.down.n) + 2*(math.sqrt(math.log(node.down.prev.n)/node.down.n))

                if (calc1 > calc2 and calc1 > calc3 and calc1 > calc4):
                    node = node.left
                elif (calc2 > calc1 and calc2 > calc3 and calc2 > calc4):
                    node = node.right
                elif (calc3 > calc1 and calc3 > calc2 and calc3 > calc4):
                    node = node.up
                elif (calc4 > calc1 and calc4 > calc2 and calc4 > calc3):
                    node = node.down
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
            simulation = self.simulation(node.state)
            while (node != None):
                node.t += simulation
                node.n += 1
                node = node.prev
            self.tree.game.restartSimulation()

        else:
            self.expand(node)
            if (node.up.n > node.down.n):
                node = node.down
            elif (node.left.n > node.right.n):
                node = node.right
            elif (node.right.n > node.up.n):
                 node = node.up
            else:
                node = node.left

            simulation = self.simulation(node.state)
            while (node != None):
                node.t += simulation
                node.n += 1
                node = node.prev
            self.tree.game.restartSimulation()

    
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
    #while (ia.tree.game.gameOverWin(False) == False and ia.tree.game.gameOverLose(False) == False):
    #    while(times > count):
    #        ia.select()
    #        count += 1
    #    ia.tree.makeMoves()
    #    print(ia.tree.game.score)
    #    count = 0
    
    while times > count:
        print(ia.simulation())
        count += 1

main()
