#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
  count = 0
  valley = 0
  inValley = False
  d = list(s)
  for move in d:
    if move =='U':
      count += 1
    elif move == 'D':
      count -= 1
    else:
      print('BAD DATA: MOVING ON')
    if inValley == False and count < 0:
      #print('IN A VALLEY')
      valley += 1
      inValley = True
    if inValley == True and count == 0:
      #print('EXITING VALLEY')
      inValley = False
  return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
