# 本題解的太冗長，程式碼應該有精簡空間
import sys
for num in sys.stdin:
    num1 = int(num)
    num2 = 0
    save = [] #使用List
    while(num2==0):
        for i in range(2,num1+1):

            if num1 == i:
                save.append(str(i))
                num2 =1
                break
            elif num1 % i == 0 and num1 != i:
                save.append(str(i))
                num1 = int(num1/i)
                break
            else:
                continue
    a=1
    b=0
    for i in range(len(save)):  
        if i+1<len(save):
            if save[i] == save[i+1]:
                a=a+1
                continue
        
        if b !=0:
            print(" * ",end="")
            if a==1:
                print(save[i],end="")
                b=b+1
            elif a !=1:
                print(save[i]+"^"+str(a),end="")
                a=1
                b=b+1
        else:
            if a==1:
                print(save[i],end="")
                b=b+1
            elif a !=1:
                print(save[i]+"^"+str(a),end="")
                a=1
                b=b+1
    print()#用來做換行用
