#
# Author: Mounceph Morssaoui
# Github: Mounceph99
# Last modified: May 14, 2020
#
# Description:
# This script generates and stores Sudoku boards of differents in their respective files.


# Import my SudokuSolver Code
from SudokuSolver import *

#Creating a list to hold the levels of Sudoku board
list_lvl = ['easy','normal','hard']

for level in list_lvl:

    print("Im starting with " + level + " boards")
    #Open file stream of the respective level sudoku
    filename = level.capitalize() + "Sudoku.txt"
    sudokuFile = open(filename, "a")
            
     #Generate 15 Sudokus for the current level and store the board and solution
     #in its file
    for i in range(0,15):
        result = init_board(lvl = level, generating = True)
        game = result[0].copy()
        sol = result[1].copy()
        sudokuFile.write(toString_sudoku(game))
        sudokuFile.write(toString_sudoku(sol))
        sudokuFile.write("\n")

    sudokuFile.close()
    print("Im done with " + level + " boards\n")
   
#end


      