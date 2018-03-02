import sys

for num in sys.stdin:
    a = num.replace("\r\n","")
    if '.' in a:
        break
    else:
        a=int(a)
        
        for i in range(1,a):
            if i%7 != 0:
                print(i,end=" ")
            else:
                continue
            
    print()
