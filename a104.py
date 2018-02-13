import sys
NumList = []

for num in sys.stdin:
    NumList += map(int,num.replace("/n","").split())

isover = True
while(isover):
    trans = NumList[1:int(NumList[0])+1]
    trans.sort()
    for x in trans:
        print(str(x),end=' ')

    for i in range(int(NumList[0])+1):
        NumList.pop(0)
        
    isover = False if len(NumList)==0 else True
    print() if isover == True else ""
