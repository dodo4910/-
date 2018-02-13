#矩陣的翻轉
import sys
NumList = []
for num in sys.stdin:
    NumList += num.split()

isover = True
while(isover):
    row = int(NumList[0])
    col = int(NumList[1])
    ori = [[0]*col for i in range(row)]
    plus = 0
    
    for j in range(row):
        for i in range(col):
            ori[j][i] = NumList[2+plus]
            plus += 1
            
    for j in range(col):
        for i in range(row):
            print(ori[i][j],end='')
            "" if i==row-1 else print(" ",end='')
        "" if j == col-1 else print() 
    
    for i in range(2+col*row):
        NumList.pop(0)

    isover = False if len(NumList)==0 else True
    print() if isover == True else ""
