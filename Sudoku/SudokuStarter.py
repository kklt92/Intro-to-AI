#!/usr/bin/env python
import struct, string, math, copy
import time

class SudokuBoard:
    """This will be the sudoku board game object your player will manipulate."""
  
    def __init__(self, size, board):
      """the constructor for the SudokuBoard"""
      self.BoardSize = size #the size of the board
      self.CurrentGameBoard= board #the current state of the game board

    def set_value(self, row, col, value):
        """This function will create a new sudoku board object with the input
        value placed on the GameBoard row and col are both zero-indexed"""

        #add the value to the appropriate position on the board
        self.CurrentGameBoard[row][col]=value
        #return a new board of the same size with the value added
        return SudokuBoard(self.BoardSize, self.CurrentGameBoard)
                                                                  
                                                                  
    def print_board(self):
        """Prints the current game board. Leaves unassigned spots blank."""
        div = int(math.sqrt(self.BoardSize))
        dash = ""
        space = ""
        line = "+"
        sep = "|"
        for i in range(div):
            dash += "----"
            space += "    "
        for i in range(div):
            line += dash + "+"
            sep += space + "|"
        for i in range(-1, self.BoardSize):
            if i != -1:
                print "|",
                for j in range(self.BoardSize):
                    if self.CurrentGameBoard[i][j] > 9:
                        print self.CurrentGameBoard[i][j],
                    elif self.CurrentGameBoard[i][j] > 0:
                        print "", self.CurrentGameBoard[i][j],
                    else:
                        print "  ",
                    if (j+1 != self.BoardSize):
                        if ((j+1)//div != j/div):
                            print "|",
                        else:
                            print "",
                    else:
                        print "|"
            if ((i+1)//div != i/div):
                print line
            else:
                print sep

def parse_file(filename):
    """Parses a sudoku text file into a BoardSize, and a 2d array which holds
    the value of each cell. Array elements holding a 0 are considered to be
    empty."""

    f = open(filename, 'r')
    BoardSize = int( f.readline())
    NumVals = int(f.readline())

    #initialize a blank board
    board= [ [ 0 for i in range(BoardSize) ] for j in range(BoardSize) ]

    #populate the board with initial values
    for i in range(NumVals):
        line = f.readline()
        chars = line.split()
        row = int(chars[0])
        col = int(chars[1])
        val = int(chars[2])
        board[row-1][col-1]=val
    
    return board
    
def is_complete(sudoku_board):
    """Takes in a sudoku board and tests to see if it has been filled in
    correctly."""
    BoardArray = sudoku_board.CurrentGameBoard
    size = len(BoardArray)
    subsquare = int(math.sqrt(size))

    #check each cell on the board for a 0, or if the value of the cell
    #is present elsewhere within the same row, column, or square
    for row in range(size):
        for col in range(size):
            if BoardArray[row][col]==0:
                return False
            for i in range(size):
                if ((BoardArray[row][i] == BoardArray[row][col]) and i != col):
                    return False
                if ((BoardArray[i][col] == BoardArray[row][col]) and i != row):
                    return False
            #determine which square the cell is in
            SquareRow = row // subsquare
            SquareCol = col // subsquare
            for i in range(subsquare):
                for j in range(subsquare):
                    if((BoardArray[SquareRow*subsquare+i][SquareCol*subsquare+j]
                            == BoardArray[row][col])
                        and (SquareRow*subsquare + i != row)
                        and (SquareCol*subsquare + j != col)):
                            return False
    return True

def init_board(file_name):
    """Creates a SudokuBoard object initialized with values from a text file"""
    board = parse_file(file_name)
    return SudokuBoard(len(board), board)

def solve(initial_board, forward_checking = False, MRV = False, MCV = False,
    LCV = False):
    """Takes an initial SudokuBoard and solves it using back tracking, and zero
    or more of the heuristics and constraint propagation methods (determined by
    arguments). Returns the resulting board solution. """
    start = time.time()
    result_board, result = backtrack(initial_board, MRV,  MCV)
    print "Using time: ", time.time() - start
    return result_board

def backtrack(board, MRV, MCV):
  if is_complete(board) == True:
    return board, True
  next_row, next_col = nextEmptyPosition(board, MRV, MCV)
  for value in possible_value(next_row, next_col, board):
    new_board = copy.deepcopy(board)
    new_board.set_value(next_row, next_col, value)
    temp_board, result  = backtrack(new_board,MRV,  MCV)
    if result == True:
      return temp_board, True

  return board, False

def nextEmptyPosition(board, MRV, MCV):
  BoardArray = board.CurrentGameBoard
  size = len(BoardArray)
  subsquare = int(math.sqrt(size))

  min_remain = 10
  prev_min = min_remain
  if(MCV==False and MRV == False):
    for row in range(size):
      for col in range(size):
        if BoardArray[row][col]==0:
          return row, col
  elif(MRV == True):
    row = 0
    col = 0
    for i in range(size):
      for j in range(size):
        if BoardArray[i][j] == 0:
          if(len(possible_value(i, j, board)) < min_remain):
            row = i
            col = j
            prev_min = min_remain
            min_remain = len(possible_value(i,j, board))

  if prev_min == min_remain:
    if MCV == True:
      row = 0
      col = 0
      maxDegree = -1
      for i in range(size):
        for j in range(size):
          if BoardArray[i][j] == 0:
            if(degree(i, j, board) > maxDegree):
              row = i
              col = j
              maxDegree = degree(i,j, board)

  return row, col

def degree(row, col, board):
  BoardArray = board.CurrentGameBoard
  size = len(BoardArray)
  subsquare = int(math.sqrt(size))

  count = 0
  for i in range(size):
    if (BoardArray[row][i] != 0): 
      count += 1
    if (BoardArray[i][col] != 0):
      count += 1


  SquareRow = row // subsquare
  SquareCol = col // subsquare
  for i in range(subsquare):
    for j in range(subsquare):
      if(BoardArray[SquareRow*subsquare+i][SquareCol*subsquare+j]
          != 0):
        count += 1

  return count



def possible_value(row, col, board):
  BoardArray = board.CurrentGameBoard
  size = len(BoardArray)
  subsquare = int(math.sqrt(size))

  result = []
  constraint = []
  for i in range(size):
    constraint.append(i+1)

  temp = copy.deepcopy(constraint)
  for i in range(size):
    if BoardArray[row][i] in temp:
      temp.remove(BoardArray[row][i])
    if BoardArray[i][col] in temp:
      temp.remove(BoardArray[i][col])

  SquareRow = row // subsquare
  SquareCol = col // subsquare
  for i in range(subsquare):
    for j in range(subsquare):
      if(BoardArray[SquareRow*subsquare+i][SquareCol*subsquare+j]
          in temp):
        temp.remove(BoardArray[SquareRow*subsquare+i][SquareCol*subsquare+j])

  result = result + temp

  return result





