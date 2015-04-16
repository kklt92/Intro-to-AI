#!/usr/bin/python

import sys
import pdb

execfile("MancalaBoard.py")
mb = MancalaBoard()
mb.hostGame(MancalaPlayer(1, Player.CUSTOM, 10), wml431(2, Player.CUSTOM, 9))
