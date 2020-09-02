import sys
n = []
c = []
for linenum,i in enumerate(sys.stdin):
    if linenum==0:
	no_cases = int(i.split()[0])
	
    name = i.split(':')[0]
    n.append(name)
    cls = i.split(' ')[1]
    cls = cls.replace('upper','3')
    cls = cls.replace('middle','2')    
    cls = cls.replace('lower','1')
    c.append(cls)
    print(linenum)
 

print(n)
print(c)

