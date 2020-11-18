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

    def stack(self):
        new_matrix = [[0] *4 for _ in range(4)]
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position += 1

        self.matrix = new_matrix

    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]


    def reverse(self):
        new_matrix = []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3 - j])

        self.matrix = new_matrix

    def transpose(self):
        new_matrix = [[0] *4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]

        self.matrix = new_matrix


    def matrix_full(self):
        full = 0
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    return False
        return True

    def add_new_tile(self):
        if not self.matrix_full():
            row = random.randint(0, 3)
            col = random.randint(0, 3)
            while (self.matrix[row][col] != 0):
                row = random.randint(0, 3)
                col = random.randint(0, 3)
            self.matrix[row][col] = random.choice([2, 4])

    def left(self):
        self.stack()
        self.combine()
        self.stack()
        self.add_new_tile()
        self.gameOverWin()
        self.gameOverLose()

    def right(self):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.add_new_tile()
        self.gameOverWin()
        self.gameOverLose()

    def up(self):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.add_new_tile()
        self.gameOverWin()
        self.gameOverLose()

    def down(self):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.add_new_tile()
        self.gameOverWin()
        self.gameOverLose()

    def horizontal_move_exists(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return True

        return False

    def vertical_move_exists(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i + 1][j]:
                    return True

        return False

    def gameOverWin(self):
        if any(2048 in row for row in self.matrix):
            print("Winnerrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
            return True
        return False

    def gameOverLose(self):
        if not any(0 in row for row in self.matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists():
            return True
        return False


class Node:
    def __init__(self, state):
        self.state = state
        #t = score
        self.w = 1
        self.g = 1
        self.t = self.w/self.g
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
        self.leftNode = None
        self.rightNode = None
        self.upNode = None
        self.downNode = None
        self.game = GameBackground()

    def addNodes(self, root):
        self.leftNode = Node("left")
        self.leftNode.prev = root
        root.left = self.leftNode
        self.rightNode = Node("right")
        self.rightNode.prev = root
        root.right = self.rightNode
        self.downNode = Node("down")
        self.downNode.prev = root
        root.down = self.downNode
        self.upNode = Node("up")
        self.upNode.prev = root
        root.up = self.upNode

    def makeNodeRoot(self, node):
        if (node == 0):
            self.root = self.left_node
        elif (node == 1):
            self.root = self.right_node


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
        self.score = 0

    def simulation(self, moved):
        root = self.tree.root
        game = GameBackground()
        for i in range(len(moved)):
            if (moved[i].state == "left"):
                game.left()
            elif (moved[i].state == "right"):
                game.right()
            elif (moved[i].state == "up"):
                game.up()
            elif (moved[i].state == "down"):
                game.down()


        while True:
            if (game.gameOverWin() == False and game.gameOverLose() == False):
                nextMove = self.possibleStates[random.randint(0,3)]
                if (nextMove == "left"):
                    game.left()
                elif (nextMove == "right"):
                    game.right()
                elif (nextMove == "up"):
                    game.up()
                elif (nextMove == "down"):
                    game.down()

            else:
                break
        
        for i in range(len(moved)):
            if (game.gameOverWin()):
                moved[i].w += 1

            moved[i].g += 1 
            moved[i].n += 1

        return game.score

    def select(self):
        node = self.tree.root
        moved = []
        moved.append(self.tree.root)
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
                calc1 = node.left.t + (2*math.sqrt(math.log(node.left.prev.n)/node.left.n))
                calc2 = node.right.t + (2*math.sqrt(math.log(node.right.prev.n)/node.right.n))
                calc3 = node.up.t + 2*math.sqrt(math.log(node.up.prev.n)/node.up.n)
                calc4 = node.down.t + 2*math.sqrt(math.log(node.down.prev.n)/node.down.n)

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

            moved.append(node)
        
        if (node.n < 1):
            print(self.simulation(moved))
        else:
            self.expand(node)
            moved.append(node.left)
            print(self.simulation(moved))
            

            


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
    times = 10000
    count = 0
    while(count < times):
        ia.select()
        count += 1

    

main()
