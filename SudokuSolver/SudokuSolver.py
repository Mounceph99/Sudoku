#
# Author: Mounceph Morssaoui
# Github: Mounceph99
# Created: May 8, 2020
# Last modified: May 15, 2020
#
# Description:
# Sudoku API: This API offers several functions to generate sudoku boards, solve sudokus
#             and much more!!!

################################################
# Imports body section
################################################

# Import floor function from math
from math import floor

# Import random package to generate random values and initialize number
# generator
from random import seed, randint
seed()

# Import os package to clear sceen
from os import system, name


################################################
# Declaration of Variables body section
################################################

# Declaring variable that will hold an empty position of the board
empty_pos = []
# List of size one
empty_pos.append(0)

################################################
# Function body section
################################################

# This function will clear the console
def cls():
    # Windows OS
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
      

# This function initializes an empty board of sudoku
def init_empty(sudoku_board): 
    sudoku_board.clear()
    for i in range(0,81):
        sudoku_board.append(0)
    find_an_empty_square(sudoku_board)
   

# This function will return true if the board is not yet filled up, note that
# if it is the case, it will record the first free space
# from the beginning.
# Else it will return false
def find_an_empty_square(sudoku_board): 

    #Board is empty, return False
    if len(sudoku_board) == 0:
        return False

    for i in range(0,81):
            if sudoku_board[i] == 0:            
                    empty_pos[0] = i                
                    return True
    return False

# This function checks the temptative move is valid in the testing position
# All according to traditional sudoku rules
def isValidMove(sudoku_board, pos, move):
    # Defining in which row the position is from, Note that I am dividing by
    # 9 because there are 9 rows
    row = floor(pos / 9)

    # Defining in which column the position is from, Note that I am doing a
    # modulus by
    # 9 because there are 9 columns
    col = pos % 9

    #Divide the board into 9 chunks, each of 3x3.  I will number them 1 to 9,
    #from left to right, top to bottom.
    #Determining which square position belongs to
    square = get_pos_square(pos,row,col)

    #Check row
    check_row = isRowValid(sudoku_board,row,move)
    #Check column
    check_col = isColValid(sudoku_board,col,move)
    #Check respective 3x3 square
    check_square = isSquareValid(sudoku_board,square,move)

    # Move is valid, only if the three previous conditions are true
    check_move = check_row and check_col and check_square

    return check_move

# This function will return in which 'square' the position belongs to, see
# comments in function for more details
def get_pos_square(pos, row, col):

    # For some reason, the value of row/col was negative or higher than 8
    # when the board size is 9x9
    # Exit immediately
    # This code should not ever run, but it makes it robust and good for
    # testing/debugging
    if (row < 0 or col < 0 or row > 8 or col > 8):
        print("ERROR: row is " + str(row) + ", col is " + str(col))
        exit()

    # Obtain square or sector of position, for reference:
    # 1|2|3
    # 4|5|6
    # 7|8|9

    if row < 3:
        if col < 3:
            square = 1
        elif col < 6:
            square = 2
        elif col < 9:
            square = 3
    elif row < 6:
        if col < 3:
            square = 4
        elif col < 6:
            square = 5
        elif col < 9:
            square = 6       
    elif row < 9:
        if col < 3:
            square = 7
        elif col < 6:
            square = 8
        elif col < 9:
            square = 9
        
    return square

# This function verifies if the move is valid in its respective row,
# according to traditional sudoku rules
def isRowValid(sudoku_board,row, move):
    for entry in sudoku_board[row * 9:(row * 9 + 9)]:
        if entry == move:
            return False
    return True

# This function verifies if the move is valid in its respective column,
# according to traditional sudoku rules
def isColValid(sudoku_board,col, move):
    for newRow in range(0,9):
        if sudoku_board[col + newRow * 9] == move:
            return False
    return True

# This function verifies if the move is valid in its respective square,
# according to traditional sudoku rules
def isSquareValid(sudoku_board,square, move):

    # Set offset depending on the square
    if square < 4:
        rowSquareInitial = 0
    elif square < 7:
        rowSquareInitial = 27
    else:
        rowSquareInitial = 54
    
    for col in range(0,3):
        for row in range(0,3):
            # rowSquareInitial is the offset
            # ((square-1)%3)*3 is the 'square column' between the 9 squares
            # col*9 is the iteration between columns in respective square and
            # board
            # row is the iteration between row in respective square and board
            if sudoku_board[rowSquareInitial + ((square - 1) % 3) * 3 + col * 9 + row] == move:
                return False
    return True

# This function will update the board
def update_board(sudoku_board,pos,move):
    sudoku_board[pos] = move
    
 
# This function prints a dashed line to separate between each row
def print_line():
    print("\n ------------------------------------- ")

#This function prints the state of the sudoku board
def print_sudoku_board(sudoku_board):
    # Horizontal bar
    print_line()
    # Prints row
    for entry, count in zip(sudoku_board, range(1,len(sudoku_board) + 1)):
        if count % 9 == 1:
            print(end = " | ")
        print(str(entry), end=" | ")
        # Start new row
        if (count % 9) == 0:
            print_line()        
    print()


# This function will solve any solvable sudoku using an algorithm called
# backtracking

# Variables for when a board takes too long to solve, likely because it is not
# solvable
debug_counter = []
debug_counter.append(0)

def solve_sudoku(sudoku_board):

    #Given an empty board, return false
    if len(sudoku_board) == 0:
        return False

    #Base case: Stop recursing when board is filled
    if not find_an_empty_square(sudoku_board):
        
        return True
    #Save current empty position
    pos = empty_pos[0]

    #Increase recursion iteration
    debug_counter[0]+=1

    #Recursive cases:
    # Iterate from 1 to 9 inclusive because these are the only move permitted
    # in traditional Sudoku
    for move in range(1,10):
        #If temptitive move is not allowed, try the next move
        #else enter statement
        if isValidMove(sudoku_board,pos,move):
            update_board(sudoku_board,pos,move)
            if solve_sudoku(sudoku_board):
                return True
            #Limit the amount of moves to 15000, if passed, took too long to
            #solve, likely is not a valid board
            elif debug_counter[0] > 15000:
                debug_counter[0] = 0
                return False
            # Wrong move, try the next one
            update_board(sudoku_board,pos,0)
            # Backtracking occurs
    
    return False

# This function will generate a a solvable sudoku board ramdomly
# How to proceed:
# User will enter difficulty between "easy", "normal" "hard", number of slots
# filled
#   changes with difficulty -> see method "difficulty_multiplier"
# Ramdomly will generate moves on an empty board, once all moves, if board is
# valid, return board
#   Else restart
def generate_board(sudoku_board, difficulty = "easy"):
    # Initialize empty board
    init_empty(sudoku_board)
    game_board = []
    # Get difficulty multiplier and save a backup
    temp_multiplier = difficulty_multiplier(difficulty)
     
    # Loop until the board is fully generated
    while True:
        #Randomly generate positions and moves and test them, if it works
        #update
        #board
        while True:
            #Randomly generate a position and a move to play
            pos = position_generator()
            move = move_generator()
            #Check if randomly generated move is valid, if so update board
            if sudoku_board[pos] == 0 and isValidMove(sudoku_board,pos,move):
                update_board(sudoku_board,pos,move)
                break

        # Decrease remaining moves to put on board counter
        temp_multiplier -= 1

        #Once all moves are on the board, this changes according to difficulty
        # check if board is valid, and if so return board
        # Else, restart from scratch
        if temp_multiplier < 1:
            game_board = sudoku_board.copy()
            return game_board  

# This function will verify is a sudoku board has a solution
def is_valid_board(sudoku_board, temp_board):
    if solve_sudoku(temp_board):
       return True
    else:
        # Sudoku board does have a solution, clear the board
        sudoku_board.clear()
        temp_board.clear()
        return False


# This function will return randomly a value between 0 and 80 inclusive
# which is the size of a 9x9 sudoku
def position_generator():
    return randint(0,80)

# This function will return randomly a value between 1 and 9 inclusive
# which are the moves permitted in a 9x9 sudoku
def move_generator():
    return randint(1,9)

# This function returns the number of sudoku moves a board will start with
# depending on difficulty passed
# Fun facts about Sudoku:
# https://www.101computing.net/sudoku-generator-algorithm/
# The minimun of givens must be 17 in order to have a one solution sudoku
# according to the link
def difficulty_multiplier(difficulty):

    if difficulty.lower() == "easy":
        return 18
    elif difficulty.lower() == "normal":
        return 14
    elif difficulty.lower() == "hard":
        return 11
    else:
        print("ERROR: Difficulty parameter is not within permitted choices")
        exit()
 
# This function returns a sudoku  board with its solution. 
# It will first try to generate a brand new sudoku, if after 2 attempts it fails, the function
# will return a premade board stored in a file respective to the difficulty. If a new board
# is created, store that board and its solution in its file.
# 
# generating is used for the script "GenerateSudokuScript.py" when it is wanted to 
# store several sudokus with solution.           
def init_board(sudo = [],sol = [],lvl = "easy", generating = False):
    #Initialize sudoku board and its solution, by first randomly generating a
    #solvable sudoku
    print("Loading, generating a sudoku board")

    #Declare and initialize Sudoku
    sol = generate_board(sol, lvl)
    sudo = sol.copy()

    #Declare and initilize attempts
    #Note: There are 3 total attempts
    #Once attempts have run out, retrieve a pre-generated board
    attempts = 1

    while attempts <= 2 or generating:
        if is_valid_board(sol,sudo): 
            #A valid board was generated, store it in file and return board and solution as a tuple
            game_board = hole_in_board(sol,sudo)
            filename = lvl.capitalize() + "Sudoku.txt"
            sudokuFile = open(filename, "a")
            sudokuFile.write(toString_sudoku(game_board))
            sudokuFile.write(toString_sudoku(sudo))
            sudokuFile.write("\n")
            sudokuFile.close()
            #Note that game_board HERE and ONLY HERE is the game board
            #and sudo it the solution
            return game_board,sudo
            
        else:
            #Unsuccessful attempt re-init board
            print("Try again, Attempt #" + str(attempts))
            attempts +=1
            sol = generate_board(sol, lvl)
            sudo = sol.copy()

    #If it passes here, it means that a board took to long to generate
    #and a board will be retrieve from a file where boards are stored respective of level
    #The board is selected randomly from the file

    #Open file stream
    filename = lvl.capitalize() + "Sudoku.txt"
    sudokuFile = open(filename, "r")

    #Reset file pointer to the beginning of the file
    sudokuFile.seek(0,0)

    #Count number of lines in file
    num_lines = 0
    for line in sudokuFile:
        num_lines+=1

    #Reset file pointer to the beginning of the file
    sudokuFile.seek(0,0)

    #Number of games
    num_game = int(num_lines/3)

    #Randomly select one board from the file
    chosen_game = (randint(0,num_game))*3 +1
    chosen_sol = chosen_game + 1

    #Move file pointer to desired sudoku
    for line in range(0,chosen_game-1):
        sudokuFile.readline()
    
    #Store game board and solution as strings
    tempsudo = sudokuFile.readline()
    tempsol = sudokuFile.readline()

    #Convert string from file to a Sudoku board
    sudo = convert_string_to_list(tempsudo)
    sol = convert_string_to_list(tempsol)
    
    #Return pre-generated sudoku
    sudokuFile.close()
    return sudo,sol
 
# This function converts the sudoku as a string delimited by commas
# EX. [1,2,3,4,5] -> "1,2,3,4,5"
# Here it is used to store a sudoku into a file
def toString_sudoku(sudoku_board):   
    temp = ""
    # Prints row
    for index in range(0,len(sudoku_board)):
        if index == 0:
            temp = temp + str(sudoku_board[index])
        else:
            temp = (temp + "," + str(sudoku_board[index]))
    temp = temp + "\n"  
    
    return temp   

# This function converts a string into a list
# Here it is used to retrieve a sudoku or a solution from a file
def convert_string_to_list(string):
    list = []
    temp = string.split(",")
    for i in temp:
        list.append(int(i))

    return list

# This function helps generating a sudoku make faster
# Idea: Have a premade board with a solution and makes holes
# Why: Building a board from scratch has high chance of generating sudokus with no solution
# Returns a sudoku board
def hole_in_board(sudoku,sol):
    
    limit_tries = 200
    number_of_holes = 25;

    while number_of_holes != 0:
    #Randomly generate a position and a move to play
        pos = position_generator()
        move = move_generator()
        if sudoku[pos] == 0:
            sudoku[pos] = sol[pos]
            number_of_holes -=1

        limit_tries -=1
        if limit_tries < 0:
            break
  
    return sudoku

#end





    





















