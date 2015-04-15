from collections import deque

""" 2 power of n. """
def twoToTheN(n):
  """
  seems like it doesn't allow to use `result << n`,
  because in official python documents it equal to `pow(2, n)`
  otherwise it will be extremely easy.
  """
  if n == 0:
    return 1
  if n == 1:
    return 2
  
  if n%2 == 0:
    result = twoToTheN(n/2)
    return result * result
  else:
    result = twoToTheN((n-1)/2)
    return 2 * result * result

""" Calculate the mean of a list L. """
def mean(L):
  result = 0.0
  for elem in L:
    result = result + elem
  result = result / len(L)
  return result

""" Find median of the list L. """
def median(L):
  L.sort()    # sort the list first
  if len(L) % 2 == 0:   # check whether list length is even or odd
    result = (L[len(L) / 2 - 1] + L[len(L) / 2]) / 2.0
  else:
    result = L[len(L) / 2]
  
  return result

""" Breath first search """
def bfs(tree, elem):
  if len(tree) <=  0:
    print "Tree is not available, check your input"
    return

  queue = deque()
  queue.append(tree)
  while len(queue) > 0:
    node = queue.popleft()
    if isinstance(node, int): # if the node is int, then print it
      print node
      if node == elem:
        return True
    else:   # if node is not int, then add everything into queue
      for i in range (0, len(node)):
        queue.append(node[i])
  
  return False

""" Depth first search """
def dfs(tree, elem):
  if len(tree) <= 0:
    print "Tree is invalid, please check input"
    return

  stack = []
  stack.append(tree)
  while len(stack) > 0: 
    """ use first in last out to do dfs """
    node = stack.pop()
    if isinstance(node, int):
      print node
      if node == elem:
        return True
    else:
      print node[0]
      if node[0] == elem:   # print first element in the list
        return True
      for i in range (1, len(node)):  #add everything else into stack
        stack.append(node[i])

  return False


""" 
" Tic Tac Toe board game
" 
"""
class TTTBoard:
  """
  " initial with clear board 
  """
  def __init__(self):
    self.board = []
    for i in range(0, 9):
      self.board.append("*")
  
  """
  " Print board as 3 * 3 matrix.
  """
  def __str__(self):
    string = ""
    for i in range(0, 3):
      for j in range(0, 3):
        string = string + self.board[i * 3 + j] + " "  
      string = string + "\n"    # add a \n to make a new line

    return string

  """
  " set the pos to be that player.
  " Check if the pos is outbound or this pos is full.
  " Returns True if the move was made and False if not 
  """
  def makeMove(self, player, pos):
    if pos > 8 or pos < 0:
      return False
    if self.board[pos] != "*":
      return False

    self.board[pos] = player
    return True

  """
  " Returns True if player has won the game, and False if not.
  """
  def hasWon(self, player):
    data = self.board
    if data[0] == player and data[1] == player and data[2] == player:
      return True
    elif data[3] == player and data[4] == player and data[5] == player:
      return True
    elif data[6] == player and data[7] == player and data[8] == player:
      return True
    elif data[0] == player and data[3] == player and data[6] == player:
      return True
    elif data[1] == player and data[4] == player and data[7] == player:
      return True
    elif data[2] == player and data[5] == player and data[8] == player:
      return True
    elif data[0] == player and data[4] == player and data[8] == player:
      return True
    elif data[2] == player and data[4] == player and data[6] == player:
      return True
    else:
      return False


  """
  " Returns True if someone has won or if the board is full, 
  " False otherwise
  """
  def gameOver(self):
    if self.hasWon("X") or self.hasWon("O"):
      return True
    for i in range (0, len(self.board)):
      if self.board[i] == "*":
        return False

    return True

  """
  " Clears the board to reset the game
  """
  def clear(self):
    for i in range(0, len(self.board)):
      self.board[i] = "*"


