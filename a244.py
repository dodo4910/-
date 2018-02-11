import sys

for num in sys.stdin:
    num_list = num.replace("\n"," ").split()
    if len(num_list)== 1:
        a,b,c=0,0,0
    else:
        a,b,c=map(int,num_list)
    
    if a == 1:
        print(int(b+c))
    elif a == 2:
        print(int(b-c))
    elif a == 3:
        print(int(b*c))
    elif a == 4:
        print(int(b/c))
    else:
        continue
