
################################################
# Imports body section
################################################
# Import package to print in colors
# Ex. print(Fore.GREEN + "Hello World") will print in green
# from colorama import init, deinit, Fore, Back, Style

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
solution_board = []
# Declaring variable that will hold an empty position of the board
empty_pos = []
empty_pos.append(99)

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
    sleep(0.01)

# This function will initialize the board to an unsovable
# board, this function is only used fro testing purposes
def initialize_board_no_solution():
    sudoku_board.extend([0,7,0,0,0,6,0,0,0,
                         9,0,0,0,0,0,0,4,1,
                         0,0,8,0,0,9,0,5,0,
                         0,9,0,0,0,7,0,0,2,
                         0,0,3,0,0,0,8,0,0,
                         4,0,0,8,0,0,0,1,0,
                         0,8,0,3,0,0,9,0,0,
                         1,6,0,0,0,0,0,0,7,
                         0,0,0,5,0,0,0,8,0])
    find_an_empty_square()
    

# Initializes board to a sudoku game, found online
# Used for testing purposes
def initialize_board_predetermined():
    sudoku_board.extend([0,0,6,1,0,2,5,0,0,
                         0,3,9,0,0,0,1,4,0,
                         0,0,0,0,4,0,0,0,0,
                         9,0,2,0,3,0,4,0,1,
                         0,8,0,0,0,0,0,7,0,
                         1,0,3,0,6,0,8,0,9,
                         0,0,0,0,1,0,0,0,0,
                         0,5,4,0,0,0,9,1,0,
                         0,0,7,5,0,3,2,0,0])
    find_an_empty_square()

# Returns solution of the board given by initialize_board_predetermined()
# Used for testing purposes
def expected_board_predetermined():
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

# This function will return true if the board is not yet filled up, note that if it is the case, it will record the first free space
# from the beginning.
# Else it will return false
def find_an_empty_square():  
    for i in range(0,81):
            if sudoku_board[i] == 0:
                empty_pos[0] = i;
                return True
    return False

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

    # Move is valid, only if the three previous conditions are true
    check_move = check_row and check_col and check_square

    return check_move

# This function will return in which 'square' the position belongs to, see comments in function for more details
def get_pos_square(pos, row, col):

    # For some reason, the value of row/col was negative or higher than 8
    # when the board size is 9x9
    # Exit immediately
    # This code should not ever run, but it makes it robust and good for testing/debugging
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
        if count%9 == 1:
            print(end = " | " )
        print(str(entry), end=" | ")
        # Start new row
        if (count%9) == 0:
            print_line()        
    print()


# This function will solve any solvable sudoku using an algorithm called
# backtracking
def solve_sudoku():
    #Base case: Stop recursing when board is filled
    if not find_an_empty_square():
        #Save solution
        solution_board.extend(sudoku_board)
        return False
    #Save current empty position
    pos = empty_pos[0]

    #Recursive cases:
    # Iterate from 1 to 9 inclusive because these are the only move permitted in traditional Sudoku
    for move in range(1,10):
        #If temptitive move is not allowed, try the next move
        #else enter statement
        if isValidMove(pos,move):
            update_board(pos,move)
            if solve_sudoku():
                return True
            # Wrong move, try the next one
            update_board(pos,0)

    # Backtracking occurs
    return False
   

  

################################################
# Main body section
################################################



init_board()
#initialize_board_no_solution()
print_sudoku_board(sudoku_board)
if solve_sudoku():
    print_sudoku_board(solution_board)
else:
    print("NO SOLUTION TO THIS BOARD")











