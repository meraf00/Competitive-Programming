# https://www.hackerrank.com/challenges/recursive-digit-sum/problem?isFullScreen=falseS
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def sum_of_digits(n):
    sum_ = 0
    for digit in n:
        sum_ += ord(digit) - 48
    return sum_

def superDigit(n, k):
    if len(n) * k == 1:
        return n
    
    sum_ = str(sum_of_digits(n) * k)        
    
    return superDigit(sum_, 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
