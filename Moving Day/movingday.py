import sys
n = []
text = []
for linenum,i in enumerate(sys.stdin):
    text.append(i)

n = int(text[0].split(' ')[0])
V = int(text[0].split(' ')[1])
boxes = []
for i in range(1,n+1):
    tx = text[i]
    v = int(tx.split(' ')[0]) *  int(tx.split(' ')[1]) *  int(tx.split(' ')[2])
    boxes.append(v-V)
    
print(max(boxes))