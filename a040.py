import sys
def fn(num):
    str_num = str(num)
    len_num = len(str_num) #確認有幾位數
    total = 0
    
    for x in range(len_num):
        total = total + int(str_num[x])**len_num
    return total

for text in sys.stdin:
    a = 0
    n,m = map(int,text.split()) #用map轉換成正整數
    for i in range(n,m):
        if i == fn(i):
            print(i,"",end="")
            a = a + 1
    
    if a == 0:
        print("none")

    print()
