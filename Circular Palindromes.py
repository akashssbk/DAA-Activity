#!/bin/python3

import os
import sys

#
# Complete the circularPalindromes function below.
#
def circularPalindromes(s):
    strs = []
    size = len(s)
    result = []
    for p in range(0,size):
        if s not in strs:
            strs.append(s)
            maxlen=1
            for i in range(0,size):
                j=1
                length1=1
                length2=0
                flag1=False
                flag2=False
                while i-j>=0 and (i+j)<size:
                    if not(flag1) and s[i-j]==s[i+j]:
                        length1+=2
                    else:
                        flag1=True
                    if not(flag2) and s[i-j+1]==s[i+j]:
                        length2+=2
                    else:
                        flag2=True
                    if flag1 and flag2:
                        break
                    j+=1

                if i-j+1>=0 and i+j<size:
                    if s[i-j+1]==s[i+j]:
                        length2+=2
                if length1>maxlen:
                    maxlen=length1
                if length2>maxlen:
                    maxlen=length2
            result.append(maxlen)
            s = s[1:size]+s[0]
        else:
            strs.append(" ")
            n=strs.index(s)
            result.append(result[n])
            s = s[1:size]+s[0]
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = circularPalindromes(s)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
