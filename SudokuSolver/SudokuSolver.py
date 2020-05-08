
################################################
# Imports body section
################################################
# Import package to print in colors
# Ex. print(Fore.GREEN + "Hello World") will print in green
from colorama import init, deinit, Fore, Back, Style

# Import floor function from math 
from math import floor

# Import os package to clear sceen
from os import system, name

# Import time package to have a proper visualization of the computer 
# coming up with the solution
from time import sleep 

################################################
# Declaration of Variables body section
################################################

# Declaring sudoku board as an empty list
sudoku_board = []

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
      
# This function will force a delay after inputing a value on the board
# for better visualization
def force_delay():
    sleep(0.1)

# This function will initialize the board to zeros
def initialize_empty_sudoku_board():
    for i in range(0,9**2):            
            sudoku_board.append(0)

# Initializes board to a sudoku game, found online
def init_board():
    sudoku_board.extend([0,0,6,1,0,2,5,0,0,
                         0,3,9,0,0,0,1,4,0,
                         0,0,0,0,4,0,0,0,0,
                         9,0,2,0,3,0,4,0,1,
                         0,8,0,0,0,0,0,7,0,
                         1,0,3,0,6,0,8,0,9,
                         0,0,0,0,1,0,0,0,0,
                         0,5,4,0,0,0,9,1,0,
                         0,0,7,5,0,3,2,0,0])

# 
def expected_board():
    board =        [8,4,6,1,7,2,5,9,3,
                    7,3,9,6,5,8,1,4,2,
                    5,2,1,3,4,9,7,6,8,
                    9,6,2,8,3,7,4,5,1,
                    4,8,5,9,2,1,3,7,6,
                    1,7,3,4,6,5,8,2,9,
                    2,9,8,7,1,4,6,3,5,
                    3,5,4,2,8,6,9,1,7,
                    6,1,7,5,9,3,2,8,4]
    return board

# This function checks the temptative move is valid in the testing position
# All according to traditional sudoku rules
def isValidMove(pos, move):
    # Defining in which row the position is from, Note that I am dividing by
    # 9 because there are 9 rows
    row = floor(pos/9)

    # Defining in which column the position is from, Note that I am doing a modulus by
    # 9 because there are 9 columns
    col = pos%9

    #Divide the board into 9 chunks, each of 3x3. I will number them 1 to 9, 
    #from left to right, top to bottom.
    #Determining which square position belongs to
    square = get_pos_square(pos,row,col)

    #Check row 
    check_row = isRowValid(row,move)
    #Check column
    check_col = isColValid(col,move)
    #Check respective 3x3 square
    check_square = isSquareValid(square,move)

    check_move = check_row and check_col and check_square

    if check_move:
        update_board(pos,move)


def get_pos_square(pos, row, col):

    # For some reason, the value of row/col was negative or higher than 8
    # when the board size is 9x9
    # Exit immediately
    # This code should not ever run, but it makes it robust
    if (row < 0 or col < 0 or row > 8 or col > 8):
        print("ERROR: row is " + str(row + ", col is " + str(col)))
        exit()

    # Obtain square or sector of position, for reference:
    # 1|2|3
    # 4|5|6
    # 7|8|9

    if row < 3:
        if col < 3:
            square = 1
        elif col <6:
            square = 2
        elif col < 9:
            square = 3
    elif row < 6:
        if col < 3:
            square = 4
        elif col <6:
            square = 5
        elif col < 9:
            square = 6       
    elif row < 9:
        if col < 3:
            square = 7
        elif col <6:
            square = 8
        elif col < 9:
            square = 9
        

    return square

# This function verifies if the move is valid in its respective row,
# according to traditional sudoku rules
def isRowValid(row, move):
    for entry in sudoku_board[row*9:(row*9 + 9)]:
        if entry == move:
            return False
    return True

# This function verifies if the move is valid in its respective column,
# according to traditional sudoku rules
def isColValid(col, move):
    increment = col
    while (increment <= 80):
        if sudoku_board[increment] == move:
            return False
        increment = increment + 9
    return True

# This function verifies if the move is valid in its respective square,
# according to traditional sudoku rules
def isSquareValid(square, move):

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
            # col*9 is the iteration between columns in respective square and board
            # row is the iteration between row in respective square and board
            if sudoku_board[rowSquareInitial + ((square-1)%3)*3 + col*9 + row] == move:
                return False
    return True

# This function will update the board
def update_board(pos,move):
    sudoku_board[pos] = move;
    
 
# This function prints a dashed line to separate between each row 
# Using this function will make everything print in WHITE with a BLACK background           
def print_line():
    print("\n ------------------------------------- ")

#This function prints the state of the sudoku board
def print_sudoku_board():
    init(convert = True)
    print_line()
    for entry, count in zip(sudoku_board, range(1,len(sudoku_board) + 1)):
        if count%9 == 1:
            print(end = " | " )
        print(str(entry), end=" | ")
        if (count%9) == 0:
            print_line()
            
    print()

#def solve_sudoku():
#    for i in range(0,len(sudoku_board)):
#        isValidMove(i,i)
#        cls()
#        print_sudoku_board()
#        force_delay()

# This function will solve any solvable sudoku using an algorithm called
# backtracking
def solve_sudoku(pos, try_this_move):

    #Base case:
    if pos >= 81:
        return

    #Recursive case:
    

def solve_sudoku_buffer():
    solve_sudoku(0,1);

################################################
# Main body section
################################################



initialize_empty_sudoku_board()
print_sudoku_board()
#print("A visualization of the solution will start in 2 seconds")
#sleep(2)
#solve_sudoku()





