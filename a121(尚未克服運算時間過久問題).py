#求質數
import sys
for num in sys.stdin:
    a,b = map(int,num.split())

    total = 0
    total+=1 if a ==2 else 0
    for testnum in range(a,b+1):
        for i in range(3,testnum+1,2):
            if testnum > i**2:
                if testnum == i:
                    total+=1
                elif testnum %i == 0 and testnum != i:
                    break
                else:
                    continue
            else:
                break
    print(total)
