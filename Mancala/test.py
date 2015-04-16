#!/usr/bin/python

import sys
import pdb

execfile("MancalaBoard.py")
mb = MancalaBoard()
pdb.run(mb.hostGame(wml431(1, Player.MINIMAX, 10), wml431(2, Player.ABPRUNE, 9)))
