#
# Author: Mounceph Morssaoui
# Github: Mounceph99
# Last modified: May 14, 2020
#
# Description:
# This program offers a GUI to play Sudoku. The user can select between 3 levels
# and offers the solution by clicking on the "Answer" button
# Have fun :)

################################################
# Imports body section
################################################

# Import Tkinter built-in which is use for Python GUI programming
from tkinter import *
from tkinter import messagebox

# Import builtin GUI programming for Python
# https://www.tutorialspoint.com/python/python_gui_programming.htm
# https://www.geeksforgeeks.org/python-gui-tkinter/
# Colors: http://www.science.smith.edu/dftwiki/index.php/File:TkInterColorCharts.png
# Doc on Tkinter Button: https://effbot.org/tkinterbook/button.htm
# Button command function with param: https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
# Obtain text of button: https://stackoverflow.com/questions/26765218/get-the-text-of-a-button-widget
# Lambda button problem: https://stackoverflow.com/questions/16224368/tkinter-button-commands-with-lambda-in-python


# Import my SudokuSolver Code
from SudokuSolver import *


################################################
# Function/Class body section
################################################

#This class will create a Sudoku board GUI. Four buttons are offered of which three are to generate Sudokus at different
#levels, and the last to print the solution of the particular Sudoku. This Sudoku board plays as follow:
#Note: The rules follow traditional Sudoku rules

#1-Select a diffulty by pressing on desired level
#2-Click on a cell to change its holding value
#3-Solve the Sudoku and have fun ;)
#4- Once Solve correctly, a message will be sent congratulating the user
#5- Repeat!!!

class SudokuGUI:

    #self is equi to 'this'
    #master is equi to root
    def __init__(self, master):
        self.master = master
        #Set title of window
        self.master.title("Sudoku by Mounceph Morssaoui")
        #Set size of window
        self.master.geometry("650x737")
        #Create two white frames, center will hold the Sudoku, bottom will hold the buttons
        self.center = Frame(self.master, bg = 'white', padx=11,pady = 5)
        self.bottom = Frame(self.master, bg = 'white',padx=30,pady = 10)

        #Configure grid allocation, without the .grid(), the frames do not show up on window
        self.master.grid_rowconfigure(10,weight=1)
        self.master.grid_columnconfigure(9,weight=1)
        self.center.grid(row = 1)
        self.bottom.grid(row = 2)
        self.center.grid_columnconfigure(1,weight=1,)
        self.center.grid_rowconfigure(0,weight=1)

        #Create user buttons which will go in the bottom frame
        self.bot_buttons = {"Easy": Button(self.bottom), "Normal": Button(self.bottom), "Hard": Button(self.bottom), "Answer": Button(self.bottom)}
        
        
        
        #Configure user buttons and display them
        for i,y in zip(self.bot_buttons,range(0,len(self.bot_buttons))):
           self.bot_buttons[i].grid(row = 1, column = y, sticky = "n", padx = 19)
           self.bot_buttons[i].config(text = i, relief = "groove",height = 1, width = 10,font = ("Comic Sans MS", "12","bold"), bg = "mint cream" )
        
        #Configure action when each button are clicked
        #Action: Create a board at desired level
        self.bot_buttons["Easy"].config(command = lambda level=self.bot_buttons["Easy"].cget('text'): self.new_board(level))
        self.bot_buttons["Normal"].config(command = lambda level=self.bot_buttons["Normal"].cget('text'): self.new_board(level))
        self.bot_buttons["Hard"].config(command = lambda level=self.bot_buttons["Hard"].cget('text'): self.new_board(level))
        #Action: Show solution of the board
        self.bot_buttons["Answer"].config(command = self.answer)
 
        #Declare list for Sudoku tiles
        self.square = []
      
        #Configure Sudoku tiles as buttons
        for row in range(0,9):
            for col in range(0,9):
                #Convert 2D to 1D indices
                index = row*9 + col
                #Obtain square the tile is a part of
                shading_square = get_pos_square(index,row,col)
                #Config
                self.square.append(Button(self.center, font = ("Helvetica", "16","bold"), bg = 'mint cream', disabledforeground = "black", foreground = "dim gray", relief = 'sunken', highlightbackground='black', highlightthickness = 1, height = 2, width = 4, padx = 5, pady = 5))           
                #Set button command which increments the value the respective button holds
                #Notice the lambda: Using this allows for each button to affect itself and NOT the last button
                self.square[index].config(command = (lambda x=index: self.buffer(x)))    
                
                #Allows to properly distinguish the 3x3 squares with constrasting
                if shading_square%2 == 1:
                    self.square[index].config(bg = "white")       
                #Display tiles as a 9x9 Board                  
                self.square[index].grid(row = row, column = col)    

        #Declaring Sudoku Variable for the game board and for the solution
        self.game_board = []
        self.solution = []
        self.result = tuple()
        
    #This function calls two function, and is called when a button is clicked
    #It first increments the button value, then check if current board is solved, if it is; congratulate the user             
    def buffer(self,i):   
        self.increment(i)
        isOver = self.check_solution()
        if isOver:
            messagebox.showinfo(title = "Congrats!!!", message = "You have beaten this Sudoku board!!!")

    #Increment button value, if the block is empty, show 1, if button is pressed with
    def increment(self, i):
        if self.square[i].cget('text') == "":
            self.square[i]['text'] = 1;
        elif self.square[i].cget('text') == 9:
            self.square[i]['text'] = "";
        elif self.square[i].cget('text') != "9" :
            self.square[i]['text'] = (int(self.square[i]['text'])+1)

    #Checks if user board is solved, return true if so
    def check_solution(self):
        for row in range(0,9):
            for col in range(0,9):
                index = row*9 + col
                if self.square[index].cget('text') == "":
                    return False
                if self.solution[index] != int(self.square[index].cget('text')):
                    return False
        return True

        #Generate a sudoku board of the requested level
    def new_board(self, level):
        self.solution.clear()
        self.game_board.clear()
        self.result = tuple()
        self.clear_board()
        #Reactive "Answer" button which was disable when it was last pressed
        self.bot_buttons["Answer"].config(state = "normal")
        self.result = init_board(lvl = level)
        self.game_board = self.result[0].copy()
        self.solution = self.result[1].copy()
        for row in range(0,9):
            for col in range(0,9):
                index = row*9 + col
                if (len(self.game_board) > 0 and self.game_board[index] != 0):
                    self.square[index].config(state = "disable", text = str(self.game_board[index]), font = ("Helvetica", "16", "bold"))



    #Display an empty board
    def clear_board(self):
        for row in range(0,9):
            for col in range(0,9):
                index = row*9 + col
                self.square[index].config(text = "", state = "normal", fg = "dim gray", disabledforeground = "black")

    #Display solution from where the user was, Tiles that are with the wrong answer including empty tiles, will show in red
    #while tiles with the right answer are shown green 
    def answer(self):
        for row in range(0,9):
            for col in range(0,9):
                index = row*9 + col
                if self.square[index].cget('text') == "" or int(self.square[index].cget('text')) != self.solution[index]:
                    self.square[index].config(disabledforeground = "red", text = self.solution[index], state = "disable")
                else:
                    if self.game_board[index] == 0:
                        self.square[index].config(disabledforeground = "green", text = self.solution[index],state = "disable")
        self.bot_buttons["Answer"].config(state = "disable")               
    


################################################
# Main body section
################################################

#Code to create and start the Sudoku GUI
root = Tk()
sudokuGUI = SudokuGUI(root)
root.mainloop()

#end