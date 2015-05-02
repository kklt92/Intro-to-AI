#!/usr/bin/python

from SudokuStarter import *
import sys
import time
import glob
import os

def main(argv):
  os.chdir(argv[0])
  for filename in glob.glob("*.sudoku"):
    Test(filename)

def Test(filename):
  forward_check = False
  MCV = False
  MRV = False
  LCV = False
  print "---------------------------------"
  print "File: ", filename
  #for i in range(4):
  print "Configure:", "Forward Checking:", forward_check, \
      ",MCV:", MCV, ",MRV:", MRV, ",LCV:", LCV
  sb = init_board(filename)
  start = time.time()
  fb = solve(sb, forward_check, MCV, MRV, LCV)
  print "Using time: %.4fs" %(time.time() - start)
  #fb.print_board()
  print "Complete: ", is_complete(fb)
  print "Counter: ", fb.counter
  
  

if __name__=="__main__":
  main(sys.argv[1:])
  
