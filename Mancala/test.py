#!/usr/bin/python

import sys
import pdb

execfile("MancalaBoard.py")
mb = MancalaBoard()
#mb.hostGame(MancalaPlayer(1, Player.ABPRUNE, 9), wml431(2, Player.CUSTOM))
mb.hostGame(wml431(1, Player.CUSTOM), wml431(2, Player.ABPRUNE, 8))
