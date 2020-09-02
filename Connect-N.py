# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:43:46 2020

@author: frmendes
"""

#import numpy as np

#def check(sub,sym):
#    if  sum(np.sum(sub==sym,axis=0) == sub.shape[0])>0:
#        return(True)
#    elif  sum(np.sum(sub==sym,axis=1) == sub.shape[0])>0:
#        return(True)
#    elif sum(np.fliplr(sub).diagonal()==sym)==sub.shape[0]:
#        return(True)
#    elif sum(sub.diagonal()==sym)==sub.shape[0]:
#        return(True)
#    else:
#        return(False)
#       
#def sub_columns(mat,i,j,N):
#    for i in range(0,N):
#        y.append([x[i] for x in mat])
#    return(y)
#
#y = []
#for i in range(0,N):
#   y.append([x[i][i] for x in rows])
   
def sub_mat(mat,i,j,N,sym):
   #i=0
   rows = ([list(x[j:(j+N)]) for x in mat[i:(i+N)]])  
   #print(rows)
   y = []
   for i in range(0,N):
    y.append([x[i] for x in rows])
   columns =  y 
   #print(columns)    
   
   diag2 = [rows[i][N-1-i] for i in range(0,N)]
   #print(diag2)
   diag1 =  [rows[i][i] for i in range(0,N)]
   #print(diag1)
   rows.extend(columns)
   rows.append(diag1)
   rows.append(diag2)
   #sym = ['B', 'B', 'B']
   return(sum([x== sym for x in rows]))
   
 
    
import sys
n = []
text = []
for linenum,i in enumerate(sys.stdin):
    text.append(i)
    

#text = ['3 6 3\n', 'B O O O O O\n', 'B O O O O O\n', 'B R R O O O\n']

mat = text[1:]
mat = [x.split() for x in mat]
#mat = np.array(mat)

blue = 0
red = 0
X = int(text[0].split(' ')[0])
Y = int(text[0].split(' ')[1])
N = int(text[0].split(' ')[2])
            

for i in range(0,X-N+1):
    for j in range(0,Y-N+1):
        #sub = mat[i:(i+N),j:(j+N)]
        blue = blue + sub_mat(mat,i,j,N,['B']*N)
        red = red + sub_mat(mat,i,j,N,['R']*N)
        
        
if(red>0 and blue==0):
    print('RED WINS')
    
elif(red==0 and blue>0):
    print('BLUE WINS')
else:
    print('NONE')



    

    

    