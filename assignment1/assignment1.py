from collections import deque

""" 2 power of n. """
def twoToTheN(n):
  result = 1

  """ do the bit shift until meet goal. """
  while n > 0:
    result = result << 1
    n -= 1

  return result

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
    if isinstance(node, int):
      print node
      if node == elem:
        return True
    else:
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
    node = stack.pop()
    if isinstance(node, int):
      print node
      if node == elem:
        return True
    else:
      print node[0]
      if node[0] == elem:
        return True
      for i in range (1, len(node)):
        stack.append(node[i])

  return False

class TTTBoard:
  def __init__(self):
    self.board = []
    for i in range(0, 9):
      self.board.append("*")

  def __str__(self):
    string = ""
    for i in range(0, 3):
      for j in range(0, 3):
        string = string + self.board[i * 3 + j] + " "  
      string = string + "\n"

    return string

  def makeMove(self, player, pos):
    if pos > 8 or pos < 0:
      return False
    if self.board[pos] != "*":
      return False

    self.board[pos] = player
    return True

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


  def gameOver(self):
    if self.board.hasWon("X") or self.board.hasWon("O"):
      return True
    for i in range (0, len(self.board)):
      if self.board[i] == "*":
        return False

    return True

  def clear(self):
    for i in range(0, len(self.board)):
      self.board[i] = "*"


