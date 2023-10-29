#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    return "".join([
    
    chr((ord(char) - 65 + k) % 26 + 65) if "A" <= char <= "Z" else
    
    chr((ord(char) - 97 + k) % 26 + 97) if "a" <= char <= "z" else
    
    char for char in s
    
    ])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
