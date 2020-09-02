import sys

def change_class(x):
    x = x.strip()
    x = x.replace(' class','')
    x = x.replace('upper','3')
    x = x.replace('middle','2')    
    x = x.replace('lower','1')
    return(x)
    
def buffer_string(s,N):
    d = N - len(s.replace('-',''))
    return(s + '-2'*d)
    
def bubbleSort(arr,names): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] < arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                names[j],names[j+1] = names[j+1],names[j]
                
def sort_class(names,x):
    x = [x[::-1] for x in x]
    N = max([len(x.replace('-','')) for x in x])
    x = [buffer_string(x,N) for x in x]
    x = [int(x.replace("-","")) for x in x]
    bubbleSort(x,names)
    return(names)

n = []
text = []
for linenum,i in enumerate(sys.stdin):
    text.append(i)

no_cases = int(text[0])
no_people = int(text[1])
start = 2
case = 1
end = start+no_people
while case<=no_cases:
    cases = text[(start):(end)]
    n = [x.split(':')[0] for x in cases]
    c = [change_class(x.split(':')[1]) for x in cases]
    #print(cases)  
    op = (sort_class(n,c))  
    [print(p) for p in op]   
    print("="*30) 
    if(case<no_cases):
        no_people = int(text[(end)])
        start = end + 1
        end = start+no_people
    case = case+1




