import sys
for num in sys.stdin:
    a,b = map(int,num.split())
 
    while(True):
        if b > a:
            b,a = a,b
    
        if a % b ==0:
            print(b)
            break
        else:
            a = a-int(a/b)*b
