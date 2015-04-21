# File: Player.py
# Author(s) names AND netid's: Weihao Ming -- wml431, Yang Hu -- yhx189 
# Date: 04/14/2015
# Defines a simple artificially intelligent player agent
# You will define the alpha-beta pruning search algorithm
# You will also define the score function in the MancalaPlayer class,
# a subclass of the Player class.


from random import *
from decimal import *
from copy import *
from MancalaBoard import *
import time     
import math

# a constant
INFINITY = 1.0e400

class Player:
    """ A basic AI (or human) player """
    HUMAN = 0
    RANDOM = 1
    MINIMAX = 2
    ABPRUNE = 3
    CUSTOM = 4
    
    def __init__(self, playerNum, playerType, ply=0):
        """Initialize a Player with a playerNum (1 or 2), playerType (one of
        the constants such as HUMAN), and a ply (default is 0)."""
        self.num = playerNum
        self.opp = 2 - playerNum + 1
        self.type = playerType
        self.ply = ply

    def __repr__(self):
        """Returns a string representation of the Player."""
        return str(self.num)
        
    def minimaxMove(self, board, ply):
        """ Choose the best minimax move.  Returns (score, move) """
        move = -1
        score = -INFINITY
        turn = self
        for m in board.legalMoves(self):
            #for each legal move
            if ply == 0:
                #if we're at ply 0, we need to call our eval function & return
                return (self.score(board), m)
            if board.gameOver():
                return (-1, -1)  # Can't make a move, the game is over
            nb = deepcopy(board)
            #make a new board
            nb.makeMove(self, m)
            #try the move
            opp = Player(self.opp, self.type, self.ply)
            s = opp.minValue(nb, ply-1, turn)
            #and see what the opponent would do next
            if s > score:
                #if the result is better than our best score so far, save that move,score
                move = m
                score = s
        #return the best score and move so far
        return score, move

    def maxValue(self, board, ply, turn):
        """ Find the minimax value for the next move for this player
        at a given board configuation. Returns score."""
        if board.gameOver():
            return turn.score(board)
        score = -INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in max value is: " + str(turn.score(board))
                return turn.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            s = opponent.minValue(nextBoard, ply-1, turn)
            #print "s in maxValue is: " + str(s)
            if s > score:
                score = s
        return score
    
    def minValue(self, board, ply, turn):
        """ Find the minimax value for the next move for this player
            at a given board configuation. Returns score."""
        if board.gameOver():
            return turn.score(board)
        score = INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in min Value is: " + str(turn.score(board))
                return turn.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            s = opponent.maxValue(nextBoard, ply-1, turn)
            #print "s in minValue is: " + str(s)
            if s < score:
                score = s
        return score


    # The default player defines a very simple score function
    # You will write the score function in the MancalaPlayer below
    # to improve on this function.
    def score(self, board):
        """ Returns the score for this player given the state of the board """
        if board.hasWon(self.num):
            return 100.0
        elif board.hasWon(self.opp):
            return 0.0
        else:
            return 50.0

    # You should not modify anything before this point.
    # The code you will add to this file appears below this line.

    # You will write this function (and any helpers you need)
    # You should write the function here in its simplest form:
    #   1. Use ply to determine when to stop (when ply == 0)
    #   2. Search the moves in the order they are returned from the board's
    #       legalMoves function.
    # However, for your custom player, you may copy this function
    # and modify it so that it uses a different termination condition
    # and/or a different move search order.
    def alphaBetaMove(self, board, ply):
        """ Choose a move with alpha beta pruning.  Returns (score, move) """
        #returns the score adn the associated moved

        a = -INFINITY
        b = INFINITY
        move = -1
        score = -INFINITY
        turn = self
        for m in board.legalMoves(self):
            #for each legal move
            if ply == 0:
                #if we're at ply 0, we need to call our eval function & return
                return (self.score(board), m)
            if board.gameOver():
                return (-1, -1)  # Can't make a move, the game is over
            nb = deepcopy(board)
            #make a new board
            nb.makeMove(self, m)
            #try the move
            opp = Player(self.opp, self.type, self.ply)
            s = opp.abMinValue(nb, ply-1, turn, a, b)
            #and see what the opponent would do next
            if s > score:
                #if the result is better than our best score so far, save that move,score
                move = m
                score = s
            if score >= b:
                return score, move
            a = max(a, score)
        #return the best score and move so far
        return score, move

    def abMaxValue(self, board, ply, turn, a, b): 
        if board.gameOver():
            return turn.score(board)
        score = -INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in max value is: " + str(turn.score(board))
                return turn.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            s = opponent.abMinValue(nextBoard, ply-1, turn, a, b)
            #print "s in maxValue is: " + str(s)
            if s > score:
                score = s
            if score >= b:
                return s
            a = max(a, score)
        return score


    def abMinValue(self, board, ply, turn, a, b):
        if board.gameOver():
            return turn.score(board)
        score = INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in min Value is: " + str(turn.score(board))
                return turn.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            nextBoard.makeMove(self, m)
            s = opponent.abMaxValue(nextBoard, ply-1, turn, a, b)
            #print "s in minValue is: " + str(s)
            if s < score:
                score = s
            if score <= a:
                return score
            b = min(b, score)
        return score


    def alphaBetaMoveCustom(self, board, ply):
        """ Choose a move with alpha beta pruning.  Returns (score, move) """
        #returns the score adn the associated moved

        a = -INFINITY
        b = INFINITY
        move = -1
        score = -INFINITY
        turn = self
        for m in board.legalMoves(self):
            #for each legal move
            if ply == 0:
                #if we're at ply 0, we need to call our eval function & return
                return (self.score(board), m)
            if board.gameOver():
                return (-1, -1)  # Can't make a move, the game is over
            nb = deepcopy(board)
            #make a new board
            cont = nb.makeMove(self, m)
            if cont:
                num = Player(self.num, self.type, self.ply)
                s = num.abMaxValueCustom(nb, ply-1, turn, a, b)                
            else:
                #try the move
                opp = Player(self.opp, self.type, self.ply)
                s = opp.abMinValueCustom(nb, ply-1, turn, a, b)
                #and see what the opponent would do next
            if s > score:
                #if the result is better than our best score so far, save that move,score
                move = m
                score = s
            if score >= b:
                return score, move
            a = max(a, score)
        #return the best score and move so far
        return score, move

    def abMaxValueCustom(self, board, ply, turn, a, b): 
        if board.gameOver():
            return turn.score(board)
        score = -INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in max value is: " + str(turn.score(board))
                return turn.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            cont = nextBoard.makeMove(self, m)
            if cont:
                num = Player(self.num, self.type, self.ply)
                s = num.abMaxValueCustom(nextBoard, ply-1, turn, a, b)
            else:
                s = opponent.abMinValueCustom(nextBoard, ply-1, turn, a, b)
            #print "s in maxValue is: " + str(s)
            if s > score:
                score = s
            if score >= b:
                return s
            a = max(a, score)
        return score


    def abMinValueCustom(self, board, ply, turn, a, b):
        if board.gameOver():
            return turn.score(board)
        score = INFINITY
        for m in board.legalMoves(self):
            if ply == 0:
                #print "turn.score(board) in min Value is: " + str(turn.score(board))
                return turn.score(board)
            # make a new player to play the other side
            opponent = Player(self.opp, self.type, self.ply)
            # Copy the board so that we don't ruin it
            nextBoard = deepcopy(board)
            cont = nextBoard.makeMove(self, m)
            if cont:
                num = Player(self.num, self.type, self.ply)
                s = num.abMinValueCustom(nextBoard, ply-1, turn, a, b)
            else:
                s = opponent.abMaxValueCustom(nextBoard, ply-1, turn, a, b)
            #print "s in minValue is: " + str(s)
            if s < score:
                score = s
            if score <= a:
                return score
            b = min(b, score)
        return score
                

                
    def chooseMove(self, board):
        """ Returns the next move that this player wants to make """
        #print "num: scorecup: ", board.scoreCups[self.num-1]
        #print "opp: scorecup: ", board.scoreCups[self.opp-1]
        if self.type == self.HUMAN:
            move = input("Please enter your move:")
            while not board.legalMove(self, move):
                print move, "is not valid"
                move = input( "Please enter your move" )
            return move
        elif self.type == self.RANDOM:
            move = choice(board.legalMoves(self))
            print "chose move", move
            return move
        elif self.type == self.MINIMAX:
            val, move = self.minimaxMove(board, self.ply)
            print "chose move", move, " with value", val
            return move
        elif self.type == self.ABPRUNE:
            now = time.time()
            val, move = self.alphaBetaMove(board, self.ply)
            stop = time.time() - now
            print "chose move", move, " with value", val
            print "Using time: %.2f" %  stop
            return move
        elif self.type == self.CUSTOM:
            now = time.time()
            if(self.num == 1 and self.counter == 0):
                val = 99
                move = 3
            elif(self.num == 1 and self.counter == 1):
                val = 99
                move = 6
            else:
                val, move = self.alphaBetaMoveCustom(board, 10)
            stop = time.time() - now
            #print "chose move", move, " with value", val
            #print "Using time: %.2f" %  stop
            self.counter +=1

            return move
        else:
            print "Unknown player type"
            return -1


# Note, you should change the name of this player to be your netid
class MancalaPlayer(Player):
    """ Defines a player that knows how to evaluate a Mancala gameboard
        intelligently """

    def score(self, board):
        """ Evaluate the Mancala board for this player """
        # Currently this function just calls Player's score
        # function.  You should replace the line below with your own code
        # for evaluating the board
        result =  board.scoreCups[self.num - 1] - board.scoreCups[self.opp - 1]

        return result
        
class MancalaAdvance(Player):
    """ Custom player """

    counter = 0
    def score(self, board):
        numSum = 0
        oppSum = 0
        if self.num == 1:
            numCups = board.P1Cups
            oppCups = board.P2Cups
        else:
            numCups = board.P2Cups
            oppCups = board.P1Cups
        for elem in numCups:
            numSum += elem
        for elem in oppCups:
            oppSum += elem

        result = board.scoreCups[self.num - 1] - board.scoreCups[self.opp - 1]
        result += numSum - oppSum
        result += 25 - board.scoreCups[self.opp - 1]
        return result

    
