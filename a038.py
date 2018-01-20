#--------------------【網友提供較好的解法】-----------------------
import sys
for s in sys.stdin:
    res = ""
    s = s.replace("\r\n","")
    print(int(s[::-1])) #直接轉數字輸出，這招厲害


#-------------------------【method 1】--------------------------
import sys
for text in sys.stdin:
    text2=text[::-1]
    a = 0
    for i in range(len(text2)):
        
        if text2[i] != "0": #因為是字串緣故，所以沒加""就會被忽略掉
            print(text2[i::])
            a = a+1
            break
        else:
            continue
    
    if a ==0:
        print("0")  #有點作弊的方式...，若想出更好方法在替換掉

#for i in range(num,0): 
#   print(text[i],end="")
#range 無法用於遞減
