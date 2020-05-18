# Sudoku by Mounceph Morssaoui
## Description
This program, written in Python, allows its users to play Sudoku according to the traditional. This program offers a simple and easy-to-use GUI which was made from Python built-in GUI Programming Tkinter. Three different difficulties are offered and the player can select which he would like to play on (i.e. Easy, Normal, Hard). These levels only differ in number of givens in their initial boards. 

## Algorithm to solve Sudoku
The methodology implememented for solving a Sudoku is by using an algorithm called Backtracking. The way backtracking works to solve a Sudoku is that it solves the board from top-left tile to bottom-right tile. It tries a 'move' and if the move works according to Sudoku rules, do the same on the next tile. If no moves are valid, go back a tile and continue from where it was. Repeat the process until there is a solution to the Sudoku. This algorithmn is of O(n^2). Backtracking is implemented by recursion.

Function: https://github.com/Mounceph99/Sudoku/blob/2aee1ce046cb6c56c4acf2036fadbcdd4e7e135a/SudokuSolver/SudokuSolver.py#L215

## Generation of Sudoku
This program generates its own Sudoku and randomly generating filling up the Sudoku, then solve the Sudoku, and make hole in the solution board according to the difficulty. This is faster and more reliable than purely generating a board by filling up the Sudoku with X amount of givens, because often there were no solutions. Board generated properly are stored in a file such that if the program takes too long to generate a random board, it can access randomly a pre-generated board for a faster and reliable user-experience.

Function: https://github.com/Mounceph99/Sudoku/blob/2aee1ce046cb6c56c4acf2036fadbcdd4e7e135a/SudokuSolver/SudokuSolver.py#L260

## How to play
Note: Make sure to have cloned the repo

1. Open SudokuGUI.exe. Found in folder SudokuSolver
2. Once the Sudoku GUI is open, select a level.
3. Press on a tile to increment the tile's move to 1. Press X amount of times, to have desired move. To reset tile to an empty tile, simply press on tile when it is at 9.
  
4. Repeat step 3 for all none given tiles.
5. Solve the Sudoku!!! Have fun ;)
6. Play again!!!
