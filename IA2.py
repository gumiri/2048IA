import tkinter as tk
import colors as c
import random
import math






class Game(tk.Frame):
    

    def __init__(self):
        tk.Frame.__init__(self)
        self.cells = []
        self.make_GUI()
        self.start_game()
        self.activeGUI = False
        self.initTree()
        self.soma = 0


        self.avg = 0

        times = 7000
        count = 0
        while (times > count):
            self.select()
            count += 1
            #print(self.tree.root.t / self.tree.root.n)
        #self.playTree()
        #print((self.tree.root.t ) / (self.tree.root.n + 1))
        print(self.tree.root.t)
        
            
        
        #self.master.bind("<Left>", self.left)
        #self.master.bind("<Right>", self.right)
        #self.master.bind("<Up>", self.up)
        #self.master.bind("<Down>", self.down)

        
        self.mainloop()


    def playTree(self):
        while(not self.isLeafNode() or not self.game_over()):
            if(self.tree.root.left.t > self.tree.root.right.t and self.tree.root.left.t > self.tree.root.up.t and self.tree.root.left.t > self.tree.root.down.t):
                self.left()
            elif(self.tree.root.right.t > self.tree.root.left.t and self.tree.root.right.t > self.tree.root.up.t and self.tree.root.right.t > self.tree.root.down.t):
                self.right()
            elif(self.tree.root.up.t > self.tree.root.right.t and self.tree.root.up.t > self.tree.root.left.t and self.tree.root.up.t > self.tree.root.down.t):
                self.up()
            elif(self.tree.root.down.t > self.tree.root.right.t and self.tree.root.down.t > self.tree.root.up.t and self.tree.root.down.t > self.tree.root.left.t):
                self.down()
            else:
                break


    def initTree(self):
        self.tree = Tree()
        node = Node(self.matrix, "left")
        self.tree.root = node
        self.tree.addNodes(self.matrix)


    def select(self):
        while (not self.isLeafNode()):
            if (self.tree.root.right.n >= 1 and self.tree.root.left.n >= 1 and self.tree.root.up.n >= 1 and self.tree.root.down.n >= 1):
                #calc1 = (self.tree.root.left.t / self.tree.root.left.n) + 2*(math.sqrt(math.log(self.tree.root.left.root.n)/self.tree.root.left.n))
                #calc2 = (self.tree.root.right.t/ self.tree.root.right.n) + 2*(math.sqrt(math.log(self.tree.root.right.root.n)/self.tree.root.right.n))
                #calc3 = (self.tree.root.up.t / self.tree.root.up.n) + 2*(math.sqrt(math.log(self.tree.root.up.root.n)/self.tree.root.up.n))
                #calc4 = (self.tree.root.down.t / self.tree.root.down.n) + 2*(math.sqrt(math.log(self.tree.root.down.root.n)/self.tree.root.down.n))
                calc1 = self.tree.root.left.t #/ self.tree.root.left.n
                calc2 = self.tree.root.right.t #/ self.tree.root.right.n
                calc3 = self.tree.root.up.t #/ self.tree.root.up.n
                calc4 = self.tree.root.down.t #/ self.tree.root.down.n

                if (calc1 > calc2 and calc1 > calc3 and calc1 > calc4):
                    self.tree.root = self.tree.root.left

                elif (calc2 > calc1 and calc2 > calc3 and calc2 > calc4):
                    self.tree.root = self.tree.root.right

                elif (calc3 > calc1 and calc3 > calc2 and calc3 > calc4):
                    self.tree.root = self.tree.root.up

                elif (calc4 > calc1 and calc4 > calc2 and calc4 > calc3):
                    self.tree.root = self.tree.root.down
                else:
                    if (calc1 == calc2):
                        self.tree.root = self.tree.root.left
                    elif (calc1 == calc3):
                        self.tree.root = self.tree.root.up
                    elif (calc1 == calc4):
                        self.tree.root = self.tree.root.down
                    elif (calc2 == calc3):
                        self.tree.root = self.tree.root.right
                    elif (calc2 == calc4):
                        self.tree.root = self.tree.root.down
                    elif (calc3 == calc4):
                        self.tree.root = self.tree.root.up

                    
            else:
                if (self.tree.root.right.n < 1):
                    self.tree.root = self.tree.root.right
                elif (self.tree.root.left.n < 1):
                    self.tree.root = self.tree.root.left
                elif (self.tree.root.up.n < 1):
                    self.tree.root = self.tree.root.up
                elif (self.tree.root.down.n < 1):
                    self.tree.root = self.tree.root.down
                else:
                    print(self.tree.root.right.n)
                    print(self.tree.root.left.n)
                    print(self.tree.root.up.n)
                    print(self.tree.root.down.n)
                    



        self.matrix = self.tree.root.board
        self.score = self.tree.root.t

        if (self.tree.root.n < 1):
            if (self.tree.root.play == "left"):
                self.left()
                self.tree.root.board = self.matrix
            elif (self.tree.root.play == "right"):
                self.right()
                self.tree.root.board = self.matrix
            elif (self.tree.root.play == "up"):
                self.up()
                self.tree.root.board = self.matrix
            elif (self.tree.root.play == "down"):
                self.down()
                self.tree.root.board = self.matrix

            self.matrix = self.tree.root.board
            self.score = self.tree.root.t
            score = self.simulation(self.tree.root.board)
            self.matrix = self.tree.root.board
            self.score = self.tree.root.t
            return score
        else:
            self.tree.addNodes(self.tree.root.board)
            while (self.tree.root.root != None):
                self.tree.root = self.tree.root.root
            return 0

        

    def isLeafNode(self):
        return self.tree.root.left == None and self.tree.root.right == None and self.tree.root.up == None and self.tree.root.down == None


    def simulation(self, board):
        print(board)
        possibleMoves = ["left", "right", "up", "down"]
        while (not self.game_over()):
            nextMove = possibleMoves[random.randint(0,3)]
            if (nextMove == "left"):
                self.left()
            elif (nextMove == "right"):
                self.right()
            elif (nextMove == "up"):
                self.up()
            elif (nextMove == "down"):
                self.down()
#modified: Tirei o loop
        while (self.tree.root.root != None):
            self.tree.root.t += self.score
            self.tree.root.n += 1
            self.tree.root = self.tree.root.root
        self.tree.root.t += self.score
        self.tree.root.n += 1
        return self.score

    def make_GUI(self):
        self.grid()
        self.master.title("2048")        
        
        self.main_grid = tk.Frame(
            self, bg = c.GRID_COLOR, bd = 3, width = 600, height = 600
        )
        self.main_grid.grid(pady = (100,0))
        #make grid
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg = c.EMPTY_CELL_COLOR,
                    width = 150,
                    height = 150

                )
                cell_frame.grid(row = i, column = j, padx = 5, pady = 5)
                cell_number = tk.Label(self.main_grid, bg = c.EMPTY_CELL_COLOR)
                cell_number.grid(row = i, column = j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)

        #make score header
        score_frame = tk.Frame(self)
        score_frame.place(relx = 0.5, y = 45, anchor = "center")
        tk.Label(
            score_frame,
            text = "Score",
            font = c.SCORE_LABEL_FONT
        ).grid(row = 0)
        self.score_label = tk.Label(score_frame, text = "0", font = c.SCORE_FONT)
        self.score_label.grid(row = 1)


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
        self.update_GUI()
        
        

    #Matrix Manipulation Functions
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
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    return False
        return True
    #Add a new 2 or 4 tile randonly to an empty cell
    def add_new_tile(self):
        if not self.matrix_full():
            row = random.randint(0, 3)
            col = random.randint(0, 3)
            while (self.matrix[row][col] != 0):
                row = random.randint(0, 3)
                col = random.randint(0, 3)
            self.matrix[row][col] = random.choice([2, 4])

    #Update the GUI to match the matrix
    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg = c.EMPTY_CELL_COLOR)
                    self.cells[i][j]["number"].configure(bg = c.EMPTY_CELL_COLOR, text = "")
                else:
                    self.cells[i][j]["frame"].configure(bg = c.CELL_COLORS[cell_value])
                    self.cells[i][j]["number"].configure(
                        bg = c.CELL_COLORS[cell_value],
                        fg = c.CELL_NUMBER_COLORS[cell_value],
                        font = c.CELL_NUMBER_FONTS[cell_value],
                        text = str(cell_value)
                    )
        self.score_label.configure(text = self.score)
        self.update_idletasks()


    def left(self):
        self.stack()
        self.combine()
        self.stack()
        self.add_new_tile()
        if(self.activeGUI):
            self.update_GUI()
        self.game_over()

    def right(self):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.add_new_tile()
        if(self.activeGUI):
            self.update_GUI()
        self.game_over()

    def up(self):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.add_new_tile()
        if(self.activeGUI):
            self.update_GUI()
        self.game_over()

    def down(self):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.add_new_tile()
        if(self.activeGUI):
            self.update_GUI()
        self.game_over()

    #Check if any moves are possible

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
        

    
    #Check if game is over (Win/Lose)

    def game_over(self):
        if (self.score > 200):
            self.activeGUI = True
        if any(2048 in row for row in self.matrix):
            #game_over_frame = tk.Frame(self.main_grid, borderwidth = 2)
            #game_over_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
            #tk.Label(
            #    game_over_frame,
            #    text = "You win!",
            #    font = c.GAME_OVER_FONT,
            #    fg = c.GAME_OVER_FONT_COLOR,
            #    bd = c.WINNER_BG
            #).pack()
            print("Winerrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
            return True

        elif not any(0 in row for row in self.matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists():
            #game_over_frame = tk.Frame(self.main_grid, borderwidth = 2)
            #game_over_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
            #tk.Label(
            #    game_over_frame,
            #    text = "Game over!",
            #    font = c.GAME_OVER_FONT,
            #    fg = c.GAME_OVER_FONT_COLOR,
            #    bg = c.LOSER_BG
            #).pack()
            #print("Loser")
            return True
        return False

class Node:
    def __init__(self, board, play):
        self.board = board
        self.root = None
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.t = 0
        self.n = 0
        self.play = play

class Tree:
    def __init__(self):
        self.root = None

    def addNodes(self, board):
        leftNode = Node(board, "left")
        rightNode = Node(board, "right")
        upNode = Node(board, "up")
        downNode = Node(board, "down")
        leftNode.root = self.root
        rightNode.root = self.root
        upNode.root = self.root
        downNode.root = self.root
        self.root.left = leftNode
        self.root.right = rightNode
        self.root.up = upNode
        self.root.down = downNode

class IA:
    pass


def main():
    Game()

main()
