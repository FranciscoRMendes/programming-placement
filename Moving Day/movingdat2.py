# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 09:28:30 2020

@author: frmendes
"""

3 10
1 1 2
2 2 2
3 2 1


text = ['3 10\n', '1 1 2\n', '2 2 2 \n', '3 2 1\n']
text = ['3 -1\n', '1 1 1\n', '2 2 2 \n', '3 3 3\n']

n = int(text[0].split(' ')[0])
V = int(text[0].split(' ')[1])
boxes = []
for i in range(1,n+1):
    print(i)
    tx = text[i]
    v = int(tx.split(' ')[0]) *  int(tx.split(' ')[1]) *  int(tx.split(' ')[2])
    boxes.append(v-V)
    
print(max(boxes))