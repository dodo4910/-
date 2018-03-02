import sys
import math
k=1
pri = int(input())
for i in range(0,pri):
    a = int(math.ceil(math.sqrt(float(input()))))
    b = int(math.floor(math.sqrt(float(input()))))

    
    total = 0
    for j in range(a,b+1):
        total = j**2 + total
        
    print('Case '+ str(k) +': '+str(total))
    k+=1
