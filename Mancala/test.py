#!/usr/bin/python

import sys


execfile("MancalaBoard.py")
mb = MancalaBoard()
mb.hostGame(MancalaPlayer(1, Player.ABPRUNE, 11), MancalaPlayer(2, Player.MINIMAX, 6))
