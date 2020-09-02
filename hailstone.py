# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 00:20:04 2020

@author: frmendes


If n=1, the sequence is composed of a single integer: 1

If n is even, the sequence is composed of n followed by sequence h(n/2)

If n is odd, the sequence is composed of n followed by sequence h(3⋅n+1)

global sum 
"""

import sys
n = []
text = []
for linenum,i in enumerate(sys.stdin):
    text.append(i)

x = int(text[0].split(' ')[0])

def hailstone(s,n):
    if n==1:
        s = s+1
        return(s)
    elif n%2==0:
        s = n + hailstone(s,n/2)
        return(s)
    elif n%2 !=0:
        s = n + hailstone(s,3*n + 1)
        return(s)

print(int(hailstone(0,x)))

