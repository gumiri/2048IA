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

        while (not self.game_over()):
            self.update()
            self.select()
            print(self.matrix)
        
        self.mainloop()

    def select(self):
        avgLeft = 0
        avgRight = 0
        avgUp = 0
        avgDown = 0
        
        matrix = self.matrix
        score = self.score

        times = 50
        count = 0
        for i in range(4):
            while (times > count):
                if (i == 0):
                    avgLeft += self.simulation(self.matrix, "left")
                    self.matrix = matrix
                    self.score = score
                    count += 1
                elif (i == 1):
                    avgRight += self.simulation(self.matrix, "right")
                    self.matrix = matrix
                    self.score = score
                    count += 1
                elif (i == 2):
                    avgUp += self.simulation(self.matrix, "up")
                    self.matrix = matrix
                    self.score = score
                    count += 1
                elif (i == 3):
                    avgDown += self.simulation(self.matrix, "down")
                    self.matrix = matrix
                    self.score = score
                    count += 1
            count = 0
        avgLeft = avgLeft / times
        avgRight = avgRight / times
        avgUp = avgUp / times
        avgDown = avgDown / times
        
        self.activeGUI = True
        if (avgLeft > avgRight and avgLeft > avgUp and avgLeft > avgDown):
            self.left()
            print("left")
        elif (avgRight > avgLeft and avgRight > avgUp and avgRight > avgDown):
            self.right()
            print("right")
        elif (avgUp > avgRight and avgUp > avgLeft and avgUp > avgDown):
            self.up()
            print("up")
        elif (avgDown > avgRight and avgDown > avgUp and avgDown > avgLeft):
            self.down()
            print("down")
        else:
            if (avgLeft == avgRight):
                self.right()
            elif (avgLeft == avgUp):
                self.up()       
            elif (avgLeft == avgDown):
                self.left()
            elif (avgRight == avgUp):
                self.right()       
            elif (avgRight == avgDown):
                self.down()
            elif (avgUp == avgDown):
                self.down()       


    def simulation(self, board, move):
        self.activeGUI = False
        if (move == "left"):
            self.left()
        elif (move == "right"):
            self.right()
        elif (move == "up"):
            self.up()
        elif (move == "down"):
            self.down()
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
        if any(2048 in row for row in self.matrix):
            if (self.activeGUI):
                game_over_frame = tk.Frame(self.main_grid, borderwidth = 2)
                game_over_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
                tk.Label(
                    game_over_frame,
                    text = "You win!",
                    font = c.GAME_OVER_FONT,
                    fg = c.GAME_OVER_FONT_COLOR,
                    bg = c.WINNER_BG
                ).pack()
            print("Winer")
            return True

        elif not any(0 in row for row in self.matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists():
            if (self.activeGUI):
                game_over_frame = tk.Frame(self.main_grid, borderwidth = 2)
                game_over_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
                tk.Label(
                    game_over_frame,
                    text = "Game over!",
                    font = c.GAME_OVER_FONT,
                    fg = c.GAME_OVER_FONT_COLOR,
                    bg = c.LOSER_BG
                ).pack()
            return True
        return False

def main():
    Game()

if __name__ == "__main__":
    main()
