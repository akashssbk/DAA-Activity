#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = s.replace(" ","")
    a = len(s)
    x = math.floor(math.sqrt(a))
    y = math.ceil(math.sqrt(a))
    if x*y<a:
        x=x+1
    ans = ""
    for i in range(0,y):
        for j in range(0,x):
            pos = j*y+i
            if pos<a:
                ans+=s[j*y+i]
        ans+=" "
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
